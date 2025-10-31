"""
Tool abstractions and built-in tools for the ReAct framework.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Callable
import re


class Tool(ABC):
    """
    Abstract base class for tools that can be used by the ReAct agent.
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the tool."""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Return a description of what the tool does."""
        pass
    
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the tool with the given arguments."""
        pass


class ToolRegistry:
    """
    Registry for managing available tools.
    """
    
    def __init__(self):
        self._tools: Dict[str, Tool] = {}
    
    def register(self, tool: Tool) -> None:
        """Register a new tool."""
        self._tools[tool.name] = tool
    
    def get(self, name: str) -> Tool:
        """Get a tool by name."""
        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found")
        return self._tools[name]
    
    def list_tools(self) -> List[str]:
        """List all registered tool names."""
        return list(self._tools.keys())
    
    def get_tools_description(self) -> str:
        """Get a formatted description of all tools."""
        descriptions = []
        for tool in self._tools.values():
            descriptions.append(f"- {tool.name}: {tool.description}")
        return "\n".join(descriptions)


class CalculatorTool(Tool):
    """
    A simple calculator tool for basic arithmetic operations.
    """
    
    @property
    def name(self) -> str:
        return "calculator"
    
    @property
    def description(self) -> str:
        return "Performs basic arithmetic calculations. Input should be a mathematical expression (e.g., '2 + 2', '10 * 5')."
    
    def execute(self, expression: str) -> Any:
        """Execute a mathematical expression."""
        try:
            # Simple safety check - only allow numbers and basic operators
            if not re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expression):
                return "Error: Invalid expression. Only numbers and +, -, *, /, (), . are allowed."
            
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error calculating: {str(e)}"


class SearchTool(Tool):
    """
    A mock search tool (placeholder for actual search implementation).
    """
    
    @property
    def name(self) -> str:
        return "search"
    
    @property
    def description(self) -> str:
        return "Searches for information on a given query. Returns mock search results."
    
    def execute(self, query: str) -> Any:
        """Execute a search query."""
        # This is a mock implementation
        return f"Mock search results for: '{query}'"


class FinishTool(Tool):
    """
    A tool to indicate that the agent has finished its task.
    """
    
    @property
    def name(self) -> str:
        return "finish"
    
    @property
    def description(self) -> str:
        return "Signals that the task is complete and returns the final answer."
    
    def execute(self, answer: str) -> Any:
        """Return the final answer."""
        return answer
