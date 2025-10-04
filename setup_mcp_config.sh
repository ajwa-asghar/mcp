#!/usr/bin/env bash
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.mcp
cat > ~/.mcp/config.json <<EOF
{
  "clients": {
    "fastapi-mcp": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "$ROOT"
    }
  }
}
EOF
chmod +x ~/.mcp/config.json || true
echo "Wrote ~/.mcp/config.json pointing to $ROOT/mcp_server.py"
