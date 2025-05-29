from google.adk.agents import Agent

diagnosis_agent = Agent(
    model="gemini-pro",
    name="diagnosis_agent",
    description="Analyzes medical symptoms and predicts possible diseases.",
    instruction="Given user symptoms and history, suggest probable conditions."
)
