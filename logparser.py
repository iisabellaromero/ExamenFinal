import re
from typing import List, Dict
import pprint 


def parse_log_file(file_name: str) -> List[Dict[str, str]]:
    """
    Parses a log file and returns a list of log entries as dictionaries.

    Args:
        file_name (str): The name of the log file to parse.

    Returns:
        List[Dict[str, str]]: A list of log entries, each represented as a dictionary.
    """
    log_entries = []
    # Ajustamos el patrón al formato del log proporcionado
    log_pattern = re.compile(r"^(?P<timestamp>\S+ \S+),\d+ - (?P<level>\w+) - (?P<message>.+)$")

    try:
        with open(file_name, 'r') as log_file:
            for line in log_file:
                match = log_pattern.match(line.strip())
                if match:
                    log_entry = {
                        "timestamp": match.group("timestamp"),
                        "level": match.group("level"),
                        "message": match.group("message"),
                        "file": file_name
                    }
                    log_entries.append(log_entry)
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred while parsing the log file: {e}")

    return log_entries

# Prueba el script con el archivo de logs
log_file = "log_03_12_2024.log"

# Parse the log file
log_entries = parse_log_file(log_file)

# Print the parsed log entries
for entry in log_entries:
    pprint.pprint(entry)
