# Agent - ReAct Framework

My first AI agent project implementing the ReAct (Reasoning and Acting) paradigm.

## Overview

This repository contains a basic framework for building ReAct agents. ReAct is a paradigm that combines reasoning and acting in an interleaved manner, allowing AI agents to solve complex tasks by thinking about what to do and then taking actions using available tools.

## Features

- **Modular Architecture**: Clean separation between agent logic, tools, and actions
- **Tool System**: Extensible tool registry for adding custom capabilities
- **Built-in Tools**: 
  - Calculator for arithmetic operations
  - Search (mock implementation)
  - Finish tool for task completion
- **Action-Observation Loop**: Classic ReAct pattern implementation
- **Easy to Extend**: Simple interface for creating custom tools

## Installation

```bash
# Clone the repository
git clone https://github.com/Faber-Yu/Agent.git
cd Agent

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from react_agent import ReActAgent

# Create an agent
agent = ReActAgent(verbose=True)

# Run a task
result = agent.run("Calculate 15 + 27")
print(result)
```

### Custom Tools

```python
from react_agent import ReActAgent, Tool

class MyCustomTool(Tool):
    @property
    def name(self):
        return "my_tool"
    
    @property
    def description(self):
        return "Description of what my tool does"
    
    def execute(self, **kwargs):
        # Your tool logic here
        return "result"

# Create agent with custom tool
agent = ReActAgent(tools=[MyCustomTool()])
result = agent.run("Some task")
```

## Examples

Run the example scripts:

```bash
# Basic usage examples
python examples/basic_usage.py

# Custom tool example
python examples/custom_tool.py
```

## Testing

Run the test suite:

```bash
python tests/test_basic.py
```

## Project Structure

```
Agent/
├── react_agent/          # Core framework
│   ├── __init__.py      # Package exports
│   ├── agent.py         # ReAct agent implementation
│   ├── action.py        # Action and ActionResult classes
│   └── tools.py         # Tool abstractions and built-in tools
├── examples/            # Usage examples
│   ├── basic_usage.py   # Basic examples
│   └── custom_tool.py   # Custom tool example
├── tests/               # Test suite
│   └── test_basic.py    # Basic tests
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## How It Works

The ReAct framework follows this pattern:

1. **Thought**: The agent reasons about what to do next
2. **Action**: The agent decides on and executes an action using a tool
3. **Observation**: The agent receives the result of the action
4. **Repeat**: Steps 1-3 repeat until the task is complete

```
Task → Thought → Action → Observation → Thought → Action → ... → Final Answer
```

## Extending the Framework

### Creating a Custom Tool

To create a custom tool, inherit from the `Tool` base class:

```python
from react_agent import Tool
from typing import Any

class MyTool(Tool):
    @property
    def name(self) -> str:
        return "my_tool"
    
    @property
    def description(self) -> str:
        return "What my tool does"
    
    def execute(self, **kwargs) -> Any:
        # Implementation
        return result
```

### Configuring the Agent

```python
agent = ReActAgent(
    tools=[custom_tool1, custom_tool2],  # Add custom tools
    max_iterations=10,                    # Maximum reasoning loops
    verbose=True                          # Print execution details
)
```

## Future Enhancements

- Integration with LLMs (OpenAI, Anthropic, etc.) for intelligent reasoning
- More built-in tools (web scraping, file operations, etc.)
- Advanced prompt engineering for better decision-making
- Conversation memory and context management
- Asynchronous execution support
- Tool result validation and error handling

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT License

## Acknowledgments

This framework is inspired by the ReAct paper: "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2022)
