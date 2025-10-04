#!/usr/bin/env python3
"""
Simple Gemini CLI simulator for testing MCP integration
"""
import subprocess
import json
import sys

def run_mcp_command(method, params):
    """Run MCP command through our server"""
    request = {
        "id": 1,
        "method": method,
        "params": params
    }
    
    try:
        # Run the MCP server with the request
        process = subprocess.Popen(
            ["python3", "mcp_server.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd="/home/ajwa-asghar/Documents/mcp/fastapi-mcp-assignment"
        )
        
        stdout, stderr = process.communicate(input=json.dumps(request))
        
        if stderr:
            print(f"Error: {stderr}")
            return None
            
        # The MCP server outputs "MCP Server ready" first, then the JSON response
        lines = stdout.strip().split('\n')
        json_line = None
        for line in lines:
            if line.startswith('{'):
                json_line = line
                break
                
        if json_line:
            response = json.loads(json_line)
            return response
        else:
            print(f"No JSON response found in: {stdout}")
            return None
        
    except Exception as e:
        print(f"Error running MCP command: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 gemini_cli_sim.py <command>")
        print("Commands:")
        print("  list - List available MCP servers")
        print("  call <server> <method> <params> - Call MCP method")
        return
    
    command = sys.argv[1]
    
    if command == "list":
        print("Available MCP servers:")
        print("- fastapi-mcp")
        
    elif command == "call" and len(sys.argv) >= 4:
        server = sys.argv[2]
        method = sys.argv[3]
        params_str = sys.argv[4] if len(sys.argv) > 4 else "{}"
        
        try:
            params = json.loads(params_str)
        except json.JSONDecodeError:
            print(f"Invalid JSON params: {params_str}")
            return
            
        if server == "fastapi-mcp":
            response = run_mcp_command(method, params)
            if response:
                print(json.dumps(response, indent=2))
            else:
                print("Failed to execute MCP command")
        else:
            print(f"Unknown server: {server}")
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
