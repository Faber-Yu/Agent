"""
Interactive demo of the ReAct Agent framework.
Run various tasks to see how the agent reasons and acts.
"""

import sys
import os

# Add parent directory to path to import react_agent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from react_agent import ReActAgent


def run_demo():
    """Run an interactive demonstration of various tasks."""
    
    agent = ReActAgent(verbose=True)
    
    tasks = [
        "Calculate 25 * 4",
        "Search for Python programming language",
        "Calculate (100 - 20) / 4",
        "Calculate 2 + 2 * 2",
    ]
    
    print("\n" + "="*60)
    print("REACT AGENT INTERACTIVE DEMO")
    print("="*60)
    print("\nThis demo shows how the ReAct agent handles different tasks")
    print("by alternating between reasoning (thinking) and acting (using tools).\n")
    
    for i, task in enumerate(tasks, 1):
        print("\n" + "="*60)
        print(f"DEMO {i}/{len(tasks)}")
        print("="*60)
        
        result = agent.run(task)
        
        print(f"\n📊 Summary for Task {i}:")
        print(f"   Task: {task}")
        print(f"   Result: {result}")
        print(f"   Steps taken: {len([h for h in agent.get_history() if h['type'] == 'action'])}")
        
        # Reset agent for next task
        agent.reset()
        
        if i < len(tasks):
            input("\n⏸  Press Enter to continue to next demo...")
    
    print("\n" + "="*60)
    print("DEMO COMPLETE")
    print("="*60)
    print("\nThe ReAct framework successfully demonstrated:")
    print("✓ Reasoning about different types of tasks")
    print("✓ Selecting appropriate tools (calculator, search)")
    print("✓ Executing actions and observing results")
    print("✓ Completing tasks efficiently")
    print("\nThis framework can be extended with:")
    print("• LLM integration for smarter reasoning")
    print("• More sophisticated tools")
    print("• Memory and context management")
    print("• Multi-step task planning")


if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n\nError running demo: {e}")
