"""
Simple parser for Windows Event Logs in JSON format
"""
import json

def parse_logs(file_path):
    with open(file_path, 'r') as f:
        logs = json.load(f)

    for log in logs:
        event_id = log.get('EventID', 'N/A')
        source = log.get('SourceName', 'N/A')
        message = log.get('Message', 'N/A')
        print(f"[{event_id}] {source} - {message}")

if __name__ == "__main__":
    # Example usage:
    parse_logs("sample-log.json")
