import json
import re


def log_parse_to_json(log_file_path):
    log_entries = []
    log_pattern = re.compile(
        r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] \[\/([\w_]+)\] (.+)"
    )

    with open(log_file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            match = log_pattern.match(line)
            if match:
                log_entries.append(
                    {
                        "timestamp": match.group(1),
                        "severity": match.group(2),
                        "source": match.group(3),
                        "message": match.group(4),
                    }
                )
            else:
                print(f"Line {line_number} doesn't match the pattern: {line.strip()}")

    return log_entries


# Example usage
if __name__ == "__main__":
    # Replace 'sample.log' with the actual log file path
    parsed_logs = log_parse_to_json("sample.log")
    print(json.dumps(parsed_logs, indent=4))
