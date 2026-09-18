"""Simple test: can we talk to the LLM?"""

from client import ask


def main():
    print("Sending prompt to local Ollama...")
    answer = ask("Reply with exactly: Hello, Prompt Coder is alive!")
    print("\n--- LLM Response ---")
    print(answer)
    print("--------------------")


if __name__ == "__main__":
    main()
    