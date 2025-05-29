from google.adk.agents import Agent

recommendation_agent = Agent(
    model="gemini-pro",
    name="recommendation_agent",
    description="Provides personalized health advice and follow-up schedules.",
    instruction="Give recommendations for healthy lifestyle and next appointments."
)
