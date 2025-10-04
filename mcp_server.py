#!/usr/bin/env python3
import sys
import json

def main():
    print("MCP Server ready", flush=True)

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue

        response = {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "result": {
                "message": f"Hello, you called method {request.get('method')}!"
            }
        }

        print(json.dumps(response), flush=True)

if __name__ == "__main__":
    main()
