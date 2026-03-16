import sys
import json

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")
normalized = file_path.replace("\\", "/")

if "obsidian/history/" in normalized and "Daily Log" not in normalized:
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "Reminder: you wrote a vault note. Update 00 - Index/Daily Log.md if you have not already."
        }
    }
    print(json.dumps(result))
