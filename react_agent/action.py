"""
Action and ActionResult classes for the ReAct framework.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Action:
    """
    Represents an action to be taken by the agent.
    
    Attributes:
        tool_name: Name of the tool to use
        arguments: Arguments to pass to the tool
    """
    tool_name: str
    arguments: Dict[str, Any]
    
    def __str__(self) -> str:
        return f"Action({self.tool_name}, {self.arguments})"


@dataclass
class ActionResult:
    """
    Represents the result of an action execution.
    
    Attributes:
        success: Whether the action was successful
        output: The output/result from the action
        error: Error message if the action failed
    """
    success: bool
    output: Any
    error: Optional[str] = None
    
    def __str__(self) -> str:
        if self.success:
            return f"Success: {self.output}"
        else:
            return f"Error: {self.error}"
