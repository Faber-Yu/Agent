"""
Core ReAct Agent implementation.
"""

from typing import List, Dict, Any, Optional
import re
from .action import Action, ActionResult
from .tools import Tool, ToolRegistry, CalculatorTool, SearchTool, FinishTool


class ReActAgent:
    """
    ReAct (Reasoning and Acting) Agent.
    
    This agent alternates between reasoning (thinking about what to do)
    and acting (taking actions using tools) to solve tasks.
    """
    
    def __init__(
        self,
        tools: Optional[List[Tool]] = None,
        max_iterations: int = 10,
        verbose: bool = True
    ):
        """
        Initialize the ReAct agent.
        
        Args:
            tools: List of tools available to the agent
            max_iterations: Maximum number of reasoning-acting iterations
            verbose: Whether to print detailed execution logs
        """
        self.tool_registry = ToolRegistry()
        self.max_iterations = max_iterations
        self.verbose = verbose
        
        # Register default tools
        default_tools = [
            CalculatorTool(),
            SearchTool(),
            FinishTool()
        ]
        
        for tool in default_tools:
            self.tool_registry.register(tool)
        
        # Register custom tools if provided
        if tools:
            for tool in tools:
                self.tool_registry.register(tool)
        
        self.reset()
    
    def reset(self):
        """Reset the agent's state."""
        self.history: List[Dict[str, str]] = []
        self.iteration = 0
    
    def think(self, task: str, observation: Optional[str] = None) -> str:
        """
        Reasoning step: Think about what to do next.
        
        Args:
            task: The task to accomplish
            observation: The observation from the previous action
            
        Returns:
            Thought process as a string
        """
        # This is a simple rule-based thinking process
        # In a real implementation, this would use an LLM
        
        if self.iteration == 0:
            thought = f"I need to solve the task: {task}. Let me think about what tools I need."
        elif observation:
            thought = f"Based on the observation: {observation}, I should consider my next step."
        else:
            thought = "Let me think about the next action to take."
        
        return thought
    
    def decide_action(self, task: str, thought: str, last_result: Optional[ActionResult] = None) -> Action:
        """
        Decide which action to take based on the current thought.
        
        Args:
            task: The task to accomplish
            thought: The current thought
            last_result: The result of the last action, if any
            
        Returns:
            Action to take
        """
        # This is a simplified decision process
        # In a real implementation, this would use an LLM to parse the thought
        # and decide on an action
        
        # If we have a successful result from a previous action, finish with it
        if last_result and last_result.success and self.iteration > 1:
            return Action(tool_name="finish", arguments={"answer": str(last_result.output)})
        
        # Check if task involves calculation
        if any(op in task.lower() for op in ['calculate', 'compute', '+', '-', '*', '/', 'sum', 'multiply']):
            # Extract the mathematical expression
            # Simple heuristic: look for numbers and operators
            expression_match = re.search(r'[\d\s\+\-\*\/\(\)\.]+', task)
            if expression_match:
                expression = expression_match.group(0).strip()
                return Action(tool_name="calculator", arguments={"expression": expression})
        
        # Check if task involves search
        if any(word in task.lower() for word in ['search', 'find', 'lookup', 'what is', 'who is']):
            return Action(tool_name="search", arguments={"query": task})
        
        # Default: finish with a simple response
        return Action(tool_name="finish", arguments={"answer": f"Completed task: {task}"})
    
    def execute_action(self, action: Action) -> ActionResult:
        """
        Execute an action using the appropriate tool.
        
        Args:
            action: The action to execute
            
        Returns:
            ActionResult containing the execution result
        """
        try:
            tool = self.tool_registry.get(action.tool_name)
            output = tool.execute(**action.arguments)
            return ActionResult(success=True, output=output)
        except Exception as e:
            return ActionResult(success=False, output=None, error=str(e))
    
    def run(self, task: str) -> str:
        """
        Run the ReAct agent on a given task.
        
        Args:
            task: The task to accomplish
            
        Returns:
            Final result/answer
        """
        self.reset()
        
        if self.verbose:
            print(f"\n{'='*60}")
            print(f"Task: {task}")
            print(f"{'='*60}\n")
            print(f"Available tools: {', '.join(self.tool_registry.list_tools())}\n")
        
        observation = None
        last_result = None
        
        for i in range(self.max_iterations):
            self.iteration = i + 1
            
            # Reasoning step
            thought = self.think(task, observation)
            if self.verbose:
                print(f"Thought {self.iteration}: {thought}")
            
            self.history.append({"type": "thought", "content": thought})
            
            # Acting step
            action = self.decide_action(task, thought, last_result)
            if self.verbose:
                print(f"Action {self.iteration}: {action}")
            
            self.history.append({"type": "action", "content": str(action)})
            
            # Execute action
            result = self.execute_action(action)
            last_result = result
            observation = str(result)
            
            if self.verbose:
                print(f"Observation {self.iteration}: {observation}\n")
            
            self.history.append({"type": "observation", "content": observation})
            
            # Check if task is finished
            if action.tool_name == "finish":
                if self.verbose:
                    print(f"{'='*60}")
                    print(f"Final Answer: {result.output}")
                    print(f"{'='*60}\n")
                return str(result.output)
        
        # Max iterations reached
        final_answer = "Maximum iterations reached without completing the task."
        if self.verbose:
            print(f"{'='*60}")
            print(final_answer)
            print(f"{'='*60}\n")
        
        return final_answer
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get the execution history."""
        return self.history
