import os
from typing import List, Union, Dict, Any
from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import json
import logging

logging.basicConfig(
    filename=os.path.expanduser("~/Dump/mcp.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


mcp = FastMCP("local-file-system")

IGNORE_DIRS = {"venv", "node_modules", ".git", "build"}

@mcp.tool(
    name="list_files",
    description="Lists all code files in repo (ignores venv, node_modules, .git, build)."
)
def list_files(path: str = ".") -> Union[List[str], Dict[str, Any]]:
    try:
        files = []
        for root, dirs, filenames in os.walk(path):
            # modify dirs in-place to skip ignored ones
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for fname in filenames:
                if fname.endswith((".py", ".java", ".js", ".ts")):  # only code files
                    full_path = os.path.join(root, fname)
                    files.append(full_path)
        return files
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

# Add search tool
@mcp.tool(
    name="search",
    description="Semantic search in repo files"
)
def search(query: str, top_k: int = 5):
    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents", "metadatas"]
    )

    hits = []
    for docs, metas in zip(results["documents"][0], results["metadatas"][0]):
        hits.append({
            "file": metas["file"],
            "chunk_index": metas["chunk_index"],
            "content": docs
        })

    return hits


# -------------------------------
# Config
# -------------------------------
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
REPO_PATH = os.environ.get("REPO_PATH", os.getcwd())   # passed from env or arg
EMBED_MODEL = "all-MiniLM-L6-v2"              # free, local embedding model

# Global Chroma client + collection
client = chromadb.Client()
collection = client.create_collection(
    name="repo",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(EMBED_MODEL)
)
# -------------------------------
# Chunking
# -------------------------------
def chunk_text(file: str, text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[Dict]:
    chunks = []
    start = 0
    idx = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunk = text[start:end]
        chunks.append({
            "file": file,
            "chunk_index": idx,
            "content": chunk
        })
        start += chunk_size - overlap
        idx += 1
    return chunks

# -------------------------------
# Build index (MAIN FUNCTION)
# -------------------------------
def build_index(repo_path: str = REPO_PATH):
    logging.info(f"🔍 Building index for repo: {repo_path}")
    files = list_files(repo_path)
    logging.info(f"📂 Found {len(files)} files")

    for f in files:
        logging.info(f"Indexing {f}...")
        content = read_file(f)
        if not isinstance(content, str) or not content.strip():
            logging.info(f"⚠️ Skipping {f} (not readable)")
            continue
        chunks = chunk_text(f, content)
        collection.add(
            documents=[c["content"] for c in chunks],
            metadatas=[{"file": c["file"], "chunk_index": c["chunk_index"]} for c in chunks],
            ids=[f"{f}_{c['chunk_index']}" for c in chunks]
        )
    logging.info(f"✅ Index built.")


# --- Startup: build index once ---
build_index()
all_data = collection.get(include=["documents", "metadatas"])

# =========== dumping ===========
# Expand ~ to the actual home directory
dump_file = os.path.expanduser("~/Dump/chroma_dump.json")
# Make sure the folder exists
os.makedirs(os.path.dirname(dump_file), exist_ok=True)
with open(dump_file, "w") as f:
    json.dump(all_data, f, indent=2)

logging.info(f"✅ Dumped ChromaDB contents to {dump_file}")
# =========== dumping ===========


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