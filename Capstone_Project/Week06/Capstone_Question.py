# enterprise_ai_assistant_single.py

from fastapi import FastAPI, Request
import sqlite3
from pydantic import BaseModel

app = FastAPI()

# ==============================
# CONTEXT MANAGEMENT
# ==============================
sessions = {}

def get_context(user_id):
    return sessions.get(user_id, [])

def update_context(user_id, query, response):
    if user_id not in sessions:
        sessions[user_id] = []
    sessions[user_id].append({
        "query": query,
        "response": response
    })


# ==============================
# SECURITY (RBAC)
# ==============================
def check_permission(role, tool):
    permissions = {
        "admin": ["database", "email", "file"],
        "user": ["database", "file"]
    }
    return tool in permissions.get(role, [])


class QueryRequest(BaseModel):
    user_id:str
    role: str = "user"
    query:str

# ==============================
# MCP STRUCTURE
# ==============================
def create_mcp_request(tool, context, payload):
    return {
        "tool": tool,
        "context": context,
        "payload": payload
    }

def create_mcp_response(status, message, result):
    return {
        "status": status,
        "message": message,
        "result": result
    }


# ==============================
# DATABASE TOOL
# ==============================
def db_tool(payload):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(payload["query"])
        data = cursor.fetchall()

        return create_mcp_response("success", "Data fetched", data)

    except Exception as e:
        return create_mcp_response("error", str(e), None)


# ==============================
# EMAIL TOOL
# ==============================
def email_tool(payload):
    try:
        to = payload["to"]
        subject = payload["subject"]
        body = payload["body"]

        print(f"Email sent to {to} | Subject: {subject}")

        return create_mcp_response(
            "success",
            "Email sent successfully",
            {"to": to, "subject": subject}
        )

    except Exception as e:
        return create_mcp_response("error", str(e), None)


# ==============================
# FILE TOOL
# ==============================
def file_tool(payload):
    try:
        filename = payload["filename"]

        with open(filename, "r") as f:
            content = f.read()

        return create_mcp_response(
            "success",
            "File read successfully",
            content
        )

    except Exception as e:
        return create_mcp_response("error", str(e), None)


# ==============================
# MCP CONNECTOR
# ==============================
def call_tool(tool_name, payload):

    tools = {
        "database": db_tool,
        "email": email_tool,
        "file": file_tool
    }

    if tool_name not in tools:
        return create_mcp_response("error", "Invalid tool", None)

    return tools[tool_name](payload)


# ==============================
# AI DECISION ENGINE
# ==============================
def decide_tool(user_input):

    text = user_input.lower()

    if "sales" in text:
        return {
            "tool": "database",
            "payload": {"query": "SELECT * FROM sales"}
        }

    elif "send email" in text:
        return {
            "tool": "email",
            "payload": {
                "to": "test@example.com",
                "subject": "Report",
                "body": "Sales report attached"
            }
        }

    elif "read file" in text:
        return {
            "tool": "file",
            "payload": {"filename": "sample.txt"}
        }

    else:
        return {
            "tool": None,
            "response": "This is a general AI response."
        }


# ==============================
# ROUTER + MULTI-TASK
# ==============================
def route_query(user_input, context, role):

    text = user_input.lower()

    if "email sales report" in text:

        db_res = call_tool("database", {"query": "SELECT * FROM sales"})

        if db_res["status"] == "error":
            return db_res

        email_payload = {
            "to": "boss@example.com",
            "subject": "Sales Report",
            "body": str(db_res["result"])
        }

        email_res = call_tool("email", email_payload)

        return create_mcp_response(
            "success",
            "Multi-task completed",
            {
                "data": db_res["result"],
                "email_status": email_res["message"]
            }
        )

    decision = decide_tool(user_input)

    if decision["tool"] is None:
        return create_mcp_response("success", "AI Response", decision["response"])

    if not check_permission(role, decision["tool"]):
        return create_mcp_response("error", "Access Denied", None)

    mcp_request = create_mcp_request(
        decision["tool"],
        context,
        decision["payload"]
    )

    return call_tool(mcp_request["tool"], mcp_request["payload"])


# ==============================
# API ENDPOINT
# ==============================
@app.post("/query")
async def query_handler(body: QueryRequest):

    try:
        user_id = body.user_id
        role = body.role
        user_input = body.query

        if not user_id or not user_input:
            return create_mcp_response("error", "Invalid input", None)

        context = get_context(user_id)

        response = route_query(user_input, context, role)

        update_context(user_id, user_input, response)

        return response

    except Exception as e:
        return create_mcp_response("error", str(e), None)


# ==============================
# INIT DATABASE
# ==============================
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product TEXT,
        amount INTEGER
    )
    """)

    cursor.execute("INSERT INTO sales (product, amount) VALUES ('Cup', 100)")
    cursor.execute("INSERT INTO sales (product, amount) VALUES ('Plate', 200)")

    conn.commit()
    conn.close()


init_db()
