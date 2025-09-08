import os
from typing import List, Union, Dict, Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local-file-system")

@mcp.tool(
    name="list_files",
    description="Lists all files in a specified directory.",
)
def list_files(path: str = ".") -> Union[List[str], Dict[str, Any]]:
    try:
        entries = os.scandir(path)
        return [entry.name for entry in entries if entry.is_file()]
    except Exception as e:
        return {"error": str(e)}

@mcp.tool(
    name="read_file",
    description="Reads the content of a file at the specified path.",
)
def read_file(path: str) -> Union[str, Dict[str, Any]]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return {"error": f"File not found: {path}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()


"""
{
  "mcpServers": {
    "cart-mcp": {
      "command": "/Users/Dheeraj/Documents/AI/my-mcp-server/venv/bin/python /Users/Dheeraj/Documents/AI/my-mcp-server/mcp-server-mcp.py"
    }
  }
}

 if does not work maybe try this, currently working if doesnot 
 work add this to command itself maybe 
 cd /Users/Dheeraj/Documents/AI/my-mcp-server
python3 -m venv venv
source venv/bin/activate


when used with cursor 

Query -gimme where is CartController only using mcp



I'll locate it via MCP by listing the controller directory.

[1 tool called]

Found via MCP:

- `CartController.java` at:
  `/Users/Dheeraj/Documents/Design/SpringBootQuestions/Cart/src/main/java/com/example/Cart/controller/CartController.java`

"""