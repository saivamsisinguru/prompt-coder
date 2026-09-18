# Architecture (Draft)

The agent will follow a ReAct (Reasoning + Acting) loop:

1. Receive user prompt and gather context.
2. Send to LLM with system instructions.
3. LLM decides on an action (tool call).
4. Execute tool (read file, write file, run command).
5. Feed observation back to LLM.
6. Repeat until task is complete.

## Core Components

- **Agent Loop** (`src/agent/`)
- **Tools** (`src/tools/`): read_file, write_file, edit_file, run_bash, etc.
- **LLM Interface** (`src/llm/`): connects to free APIs or local models.
- **Permission System**: asks user before dangerous commands.

## Planned Tools

- `read_file(path)`
- `write_file(path, content)`
- `edit_file(path, old, new)`
- `run_bash(command)`
- `glob(pattern)`
- `grep(pattern)`