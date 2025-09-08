#
# This script implements a simple Model Context Protocol (MCP) server
# that exposes two tools: `list_files` and `read_file`.
# It allows an AI client (like Cursor) to interact with the local file system.

# The `fastmcp` library is the standard Python SDK for building MCP servers.
# If you don't have it, you can install it using pip:
# pip install mcp-server-fastmcp

import os
from mcp.server.fastmcp import FastMCP
from typing import List, Union, Dict, Any

# Initialize the MCP server with a unique name.
# This name will be used by the AI client to identify the server.
# We also set the network host and port here.
host = "localhost"
port = 8000
mcp = FastMCP("local-file-system", host=host, port=port, stateless_http=True)

# Define and register the 'list_files' tool.
# The @mcp.tool() decorator tells the server to expose this function
# as a callable tool for the AI client.
@mcp.tool(
    name="list_files",
    description="Lists all files in a specified directory.",
)
def list_files(path: str = ".") -> Union[List[str], Dict[str, Any]]:
    """
    Lists all files (not subdirectories) in a given path.

    Args:
        path: The path to the directory. Defaults to the current directory ('.').

    Returns:
        A list of file names, or a dictionary with an 'error' key if an
        exception occurs.
    """
    try:
        # Use os.scandir for better performance, then filter for files
        entries = os.scandir(path)
        return [entry.name for entry in entries if entry.is_file()]
    except Exception as e:
        # Return a structured error message if something goes wrong.
        return {"error": str(e)}

# Define and register the 'read_file' tool.
@mcp.tool(
    name="read_file",
    description="Reads the content of a file at the specified path.",
)
def read_file(path: str) -> Union[str, Dict[str, Any]]:
    """
    Reads and returns the entire content of a file.

    Args:
        path: The full path to the file to be read.

    Returns:
        The content of the file as a string, or a dictionary with an 'error'
        key if an exception occurs.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return {"error": f"File not found: {path}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # The `mcp.run()` method now only specifies the transport.
    print(f"Server is running. Connect your agent to http://{host}:{port}/mcp/")
    mcp.run(transport='streamable-http')



"""

python mcp_server.py 

Example curl command to list tools:

curl -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}' \
  http://localhost:8000/mcp

Output:
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "list_files",
        "description": "Lists all files in a specified directory.",
        "inputSchema": {
          "properties": {
            "path": {
              "default": ".",
              "title": "Path",
              "type": "string"
            }
          },
          "title": "list_filesArguments",
          "type": "object"
        },
        "outputSchema": {
          "properties": {
            "result": {
              "anyOf": [
                {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                {
                  "additionalProperties": true,
                  "type": "object"
                }
              ],
              "title": "Result"
            }
          },
          "required": [
            "result"
          ],
          "title": "list_filesOutput",
          "type": "object"
        }
      },
      {
        "name": "read_file",
        "description": "Reads the content of a file at the specified path.",
        "inputSchema": {
          "properties": {
            "path": {
              "title": "Path",
              "type": "string"
            }
          },
          "required": [
            "path"
          ],
          "title": "read_fileArguments",
          "type": "object"
        },
        "outputSchema": {
          "properties": {
            "result": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "additionalProperties": true,
                  "type": "object"
                }
              ],
              "title": "Result"
            }
          },
          "required": [
            "result"
          ],
          "title": "read_fileOutput",
          "type": "object"
        }
      }
    ]
  }
}

Example curl command to call the list_files tool:
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "list_files", "arguments": {"path": "."}}}' \
  http://localhost:8000/mcp

Output:
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "mcp_server.py"
      }
    ],
    "structuredContent": {
      "result": [
        "mcp_server.py"
      ]
    },
    "isError": false
  }
}

Example curl command to call the read_file tool:
curl -X POST   -H "Content-Type: application/json"   -H "Accept: application/json, text/event-stream"   -d '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "read_file", "arguments": {"path": "mcp_server.py"}}}'   http://localhost:8000/mcp

Output:
event: message
data: {
"jsonrpc":"2.0","id":3,
"result":{"content":[{"type":"text","text":"<text of this file>"
}],
"isError":false
}


"""