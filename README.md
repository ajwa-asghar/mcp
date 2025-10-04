# FastAPI + MCP Server demo
This repo contains:
- a small FastAPI Todo app (app/main.py)
- an MCP server (mcp_server.py) that exposes tools and calls the FastAPI endpoints via HTTP
- scripts to create `~/.mcp/config.json` and run the demo

Quick start:
1. python -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. bash setup_mcp_config.sh
4. In a terminal run: bash run_demo.sh
5. In another terminal test: `gemini mcp list` and `gemini mcp call fastapi-mcp list_todos '{}'`

demo/ (empty)
