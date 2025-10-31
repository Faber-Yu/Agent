"""
Basic usage example of the ReAct Agent framework.
"""

import sys
import os

# Add parent directory to path to import react_agent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from react_agent import ReActAgent


def main():
    """Run basic examples of the ReAct agent."""
    
    # Create a ReAct agent
    agent = ReActAgent(verbose=True)
    
    # Example 1: Simple calculation task
    print("\n" + "="*60)
    print("EXAMPLE 1: Calculation Task")
    print("="*60)
    result = agent.run("Calculate 15 + 27")
    print(f"\nResult: {result}")
    
    # Example 2: Search task
    print("\n" + "="*60)
    print("EXAMPLE 2: Search Task")
    print("="*60)
    result = agent.run("Search for information about ReAct agents")
    print(f"\nResult: {result}")
    
    # Example 3: Complex calculation
    print("\n" + "="*60)
    print("EXAMPLE 3: Complex Calculation")
    print("="*60)
    result = agent.run("Calculate (10 + 5) * 3")
    print(f"\nResult: {result}")


if __name__ == "__main__":
    main()
