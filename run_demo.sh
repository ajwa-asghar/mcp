#!/usr/bin/env bash
set -e
# Start FastAPI in background on port 8000
uvicorn app.main:app --reload --port 8000 &
FASTAPI_PID=$!
# Start MCP server on port 8001
python mcp_server.py &
MCP_PID=$!
# Wait for both processes
wait $FASTAPI_PID $MCP_PID
