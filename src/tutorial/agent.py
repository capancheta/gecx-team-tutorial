from google.adk.agents import Agent


def create_agent() -> Agent:
    return Agent(
        name="caveman",
        model="gemini-3.5-flash-lite",
        description="""
            speak like caveman.
        """,
        instruction="",
        tools=[],
    )


root_agent = create_agent()
