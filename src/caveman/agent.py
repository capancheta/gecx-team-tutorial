from google.adk.agents import Agent


def create_agent() -> Agent:

    return Agent(
        name="caveman",
        model="gemini-2.5-pro",
        description="""
            speak like caveman.
        """,
        instruction="",
        tools=[],
    )


root_agent = create_agent()
