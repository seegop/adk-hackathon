from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime




def get_current_time() -> dict:
    """ Get the current time in a friendly formatof YYYY-MM-DD HH:MM:SS """
    return { "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") }


greeting_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash-exp",
    description="Greeting agent",
    instruction="""
    You are a greeting agent. Your task is to greet the user with a friendly message and tell a joke. : - get current time 
    """,
    # tools=[google_search],
    tools=[get_current_time],
)

