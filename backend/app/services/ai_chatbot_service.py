def get_ai_response(question: str) -> str:
    question = question.lower()

    if "carbon" in question:
        return "Reduce energy consumption, use renewable energy, and improve efficiency."

    elif "esg" in question:
        return "ESG stands for Environmental, Social, and Governance metrics."

    elif "energy" in question:
        return "Monitor energy bills regularly and optimize equipment usage."

    return f"AI Response: {question}"