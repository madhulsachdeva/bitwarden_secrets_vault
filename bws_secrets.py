import subprocess
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env from the same directory as the script

# Debug: Confirm token is loaded
# print("Token loaded:", os.getenv("BWS_ACCESS_TOKEN") is not None)
# This is to check is the BWS access token is loaded as an environment variable.


def get_bw_secret_value(secret_id: str) -> str:
    result = subprocess.run(
        ["bws", "secret", "get", secret_id, "--output", "json"],  # Force JSON output
        capture_output=True,
        text=True,
        check=True,
        env=os.environ,  # Pass the environment explicitly
    )
    return result.stdout


def clean_json(json_string):
    """
    Remove ANSI escape codes from a JSON string.

    Args:
        json_string (str): JSON string containing ANSI escape codes

    Returns:
        str: Clean JSON string without ANSI escape codes
    """
    # Pattern matches ANSI escape sequences
    ansi_escape = re.compile(r"\x1b\[[0-9;]*[a-zA-Z]|\x1b\[[0-9;]*m")

    # Remove ANSI escape codes
    clean_string = ansi_escape.sub("", json_string)

    return clean_string


def get_secret(secret_id: str):
    try:
        secret_value = get_bw_secret_value(secret_id)
        json_string = clean_json(secret_value)
        data = json.loads(json_string)
        secret = data["value"]
        return secret
    except Exception as e:
        raise Exception(f"Error: {e}")


if __name__ == "__main__":
    #Test Importing the Secrets by Secret ID from BWS Vault.
    secret_id = input("Secret ID: ")

    my_secret = get_secret(secret_id)
    print(my_secret)
