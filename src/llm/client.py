"""LLM client for Prompt Coder - connects to local Ollama."""

from openai import OpenAI


# Ollama exposes an OpenAI-compatible API on this local URL.
# It doesn't need a real API key, but the OpenAI client requires one.
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)


def ask(prompt: str, model: str = "qwen2.5-coder:7b") -> str:
    """Send a prompt to the local LLM and return its text response."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content