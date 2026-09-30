import sys
import json
import re
from datetime import datetime
from pathlib import Path

def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            print(json.dumps({"decision": "allow"}))
            return

        payload = json.loads(raw_input)
        tool_call = payload.get("toolCall", {})
        tool_name = tool_call.get("name", "")
        args = tool_call.get("args", {})

        # Workspace root is parent of scripts dir
        script_dir = Path(__file__).resolve().parent
        agents_dir = script_dir.parent
        workspace_root = agents_dir.parent
        output_file = workspace_root / "accessed_urls.md"

        # Initialize markdown file if not exists
        if not output_file.exists():
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("# Real-Time Accessed URLs & Tool Events Log\n\n")
                f.write("| Timestamp | Tool | Target / URL / Query | Event Type |\n")
                f.write("|---|---|---|---|\n")

        # Find URLs and relevant targets
        urls_found = set()
        query_found = None

        args_str = json.dumps(args)
        regex_urls = re.findall(r'https?://[^\s"\'<>\\]+', args_str)
        for u in regex_urls:
            urls_found.add(u)

        if "query" in args:
            query_found = args["query"]
        if "Arguments" in args and isinstance(args["Arguments"], dict):
            mcp_args = args["Arguments"]
            if "query" in mcp_args:
                query_found = mcp_args["query"]
            if "urls" in mcp_args and isinstance(mcp_args["urls"], list):
                for u in mcp_args["urls"]:
                    urls_found.add(u)
            if "url" in mcp_args:
                urls_found.add(mcp_args["url"])
            if "Url" in mcp_args:
                urls_found.add(mcp_args["Url"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entries = []
        if urls_found:
            for u in sorted(urls_found):
                entries.append(f"| {timestamp} | `{tool_name}` | `{u}` | Network Request / Fetch |")
        elif query_found:
            entries.append(f"| {timestamp} | `{tool_name}` | `Query: {query_found}` | Search Web Event |")
        elif tool_name in ["read_url_content", "call_mcp_tool", "web_search_exa", "web_fetch_exa"]:
            entries.append(f"| {timestamp} | `{tool_name}` | `{args_str[:80]}` | MCP / Web Tool Event |")

        if entries:
            with open(output_file, "a", encoding="utf-8") as f:
                for entry in entries:
                    f.write(entry + "\n")

    except Exception:
        pass
    finally:
        print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
