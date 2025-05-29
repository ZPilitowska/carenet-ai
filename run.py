from agents.agent_root import agent_root

if __name__ == "__main__":
    print("🩺 Welcome to Carenet-AI 🩺")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        result = agent_root.route(user_input)
        print(f"Carenet-AI: {result}")
