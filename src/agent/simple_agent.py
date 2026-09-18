"""First real agent: reads a file and asks the LLM about it."""

import sys
from pathlib import Path

# Add src/llm and src/tools to the import path so we can use them
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "llm"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from client import ask        # from src/llm/client.py
from file_tools import read_file  # from src/tools/file_tools.py


def main():
    if len(sys.argv) < 3:
        print("Usage: python simple_agent.py <file_path> \"<question>\"")
        print('Example: python simple_agent.py ../../README.md "Summarize this file in one sentence."')
        sys.exit(1)

    file_path = sys.argv[1]
    question = sys.argv[2]

    print(f"Reading file: {file_path}")
    content = read_file(file_path)

    prompt = f"""Here is the content of a file:

--- BEGIN FILE ---
{content}
--- END FILE ---

Based on this file, answer the following question:

{question}
"""

    print("Asking the LLM...\n")
    answer = ask(prompt)
    print("--- LLM Answer ---")
    print(answer)
    print("------------------")


if __name__ == "__main__":
    main()