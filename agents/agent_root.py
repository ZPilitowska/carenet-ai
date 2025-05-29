from google.adk.agents import Agent
from agents.diagnosis_agent import diagnosis_agent
from agents.recommendation_agent import recommendation_agent

class RootAgent(Agent):
    def __init__(self):
        super().__init__(
            model="gemini-pro",
            name="root_agent",
            description="Main coordinator for patient interaction.",
            instruction="Decide whether to analyze symptoms or give recommendations.",
        )

    def route(self, user_input):
        if "symptom" in user_input or "pain" in user_input or "feel" in user_input:
            return diagnosis_agent.run(user_input)
        elif "recommend" in user_input or "advice" in user_input or "next visit" in user_input:
            return recommendation_agent.run(user_input)
        else:
            return "I'm not sure which action to take. Please clarify your health concern."

root_agent = RootAgent()
