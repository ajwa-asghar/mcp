#!/usr/bin/env python3
import requests
import json

# Test FastAPI endpoints directly
print("Testing FastAPI endpoints:")
try:
    response = requests.get("http://127.0.0.1:8000/greet/Ajwa")
    print(f"Greet: {response.json()}")
except Exception as e:
    print(f"Greet error: {e}")

try:
    response = requests.get("http://127.0.0.1:8000/todos")
    print(f"List todos: {response.json()}")
except Exception as e:
    print(f"List todos error: {e}")

try:
    response = requests.post("http://127.0.0.1:8000/todos", json={"title": "Test", "description": "From Python"})
    print(f"Create todo: {response.json()}")
except Exception as e:
    print(f"Create todo error: {e}")

# Test MCP server
print("\nTesting MCP server:")
try:
    response = requests.get("http://127.0.0.1:8001/")
    print(f"MCP server: {response.text}")
except Exception as e:
    print(f"MCP server error: {e}")

