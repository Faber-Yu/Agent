"""
ReAct Agent Framework

A basic implementation of the ReAct (Reasoning and Acting) paradigm for AI agents.
ReAct combines reasoning and acting in an interleaved manner to solve tasks.
"""

from .agent import ReActAgent
from .action import Action, ActionResult
from .tools import Tool, ToolRegistry

__version__ = "0.1.0"
__all__ = ["ReActAgent", "Action", "ActionResult", "Tool", "ToolRegistry"]
