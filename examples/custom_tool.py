"""
Example of creating and using a custom tool with the ReAct Agent.
"""

import sys
import os

# Add parent directory to path to import react_agent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from react_agent import ReActAgent, Tool
from typing import Any


class WeatherTool(Tool):
    """
    A mock weather tool for demonstration purposes.
    """
    
    @property
    def name(self) -> str:
        return "weather"
    
    @property
    def description(self) -> str:
        return "Gets weather information for a given location. Returns mock weather data."
    
    def execute(self, location: str) -> Any:
        """Get weather for a location."""
        # Mock implementation
        return f"Weather in {location}: Sunny, 72°F"


class TranslateTool(Tool):
    """
    A mock translation tool for demonstration purposes.
    """
    
    @property
    def name(self) -> str:
        return "translate"
    
    @property
    def description(self) -> str:
        return "Translates text to a target language. Returns mock translation."
    
    def execute(self, text: str, target_language: str) -> Any:
        """Translate text."""
        # Mock implementation
        return f"Translation of '{text}' to {target_language}: [Mock Translation]"


def main():
    """Run example with custom tools."""
    
    # Create custom tools
    weather_tool = WeatherTool()
    translate_tool = TranslateTool()
    
    # Create agent with custom tools
    agent = ReActAgent(tools=[weather_tool, translate_tool], verbose=True)
    
    print("\n" + "="*60)
    print("CUSTOM TOOLS EXAMPLE")
    print("="*60)
    
    # The agent now has access to weather and translate tools
    # in addition to the default tools
    print("\nAvailable tools:")
    print(agent.tool_registry.get_tools_description())
    
    # Example: Use calculator (default tool)
    print("\n" + "="*60)
    print("Using default calculator tool:")
    print("="*60)
    result = agent.run("Calculate 100 / 4")
    print(f"\nResult: {result}")


if __name__ == "__main__":
    main()
