"""
Basic tests for the ReAct Agent framework.
"""

import sys
import os

# Add parent directory to path to import react_agent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from react_agent import ReActAgent, Action, ActionResult, Tool, ToolRegistry


def test_action_creation():
    """Test Action class creation."""
    action = Action(tool_name="calculator", arguments={"expression": "2 + 2"})
    assert action.tool_name == "calculator"
    assert action.arguments == {"expression": "2 + 2"}
    print("✓ test_action_creation passed")


def test_action_result():
    """Test ActionResult class."""
    result = ActionResult(success=True, output=4)
    assert result.success is True
    assert result.output == 4
    assert result.error is None
    
    error_result = ActionResult(success=False, output=None, error="Test error")
    assert error_result.success is False
    assert error_result.error == "Test error"
    print("✓ test_action_result passed")


def test_tool_registry():
    """Test ToolRegistry functionality."""
    registry = ToolRegistry()
    
    # Create a mock tool
    class MockTool(Tool):
        @property
        def name(self):
            return "mock"
        
        @property
        def description(self):
            return "A mock tool"
        
        def execute(self, **kwargs):
            return "mock result"
    
    tool = MockTool()
    registry.register(tool)
    
    assert "mock" in registry.list_tools()
    retrieved_tool = registry.get("mock")
    assert retrieved_tool.name == "mock"
    print("✓ test_tool_registry passed")


def test_calculator_tool():
    """Test the calculator tool."""
    from react_agent.tools import CalculatorTool
    
    calc = CalculatorTool()
    assert calc.name == "calculator"
    
    result = calc.execute(expression="2 + 2")
    assert result == 4
    
    result = calc.execute(expression="10 * 5")
    assert result == 50
    print("✓ test_calculator_tool passed")


def test_agent_initialization():
    """Test ReAct agent initialization."""
    agent = ReActAgent(verbose=False)
    
    # Check that default tools are registered
    tools = agent.tool_registry.list_tools()
    assert "calculator" in tools
    assert "search" in tools
    assert "finish" in tools
    print("✓ test_agent_initialization passed")


def test_agent_run():
    """Test running the agent on a simple task."""
    agent = ReActAgent(verbose=False, max_iterations=5)
    
    # Test with a calculation task
    result = agent.run("Calculate 5 + 3")
    assert result is not None
    assert len(agent.get_history()) > 0
    print("✓ test_agent_run passed")


def run_all_tests():
    """Run all tests."""
    print("\nRunning ReAct Agent Framework Tests")
    print("="*60)
    
    test_action_creation()
    test_action_result()
    test_tool_registry()
    test_calculator_tool()
    test_agent_initialization()
    test_agent_run()
    
    print("="*60)
    print("All tests passed! ✓")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_all_tests()
