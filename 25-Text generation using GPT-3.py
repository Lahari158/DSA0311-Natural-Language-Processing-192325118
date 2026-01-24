import random

def gpt3_mock(prompt):
    responses = [
        "Natural Language Processing is a field of AI that helps computers understand human language.",
        "NLP is used in chatbots, translation systems, and voice assistants.",
        "It combines linguistics, machine learning, and deep learning techniques."
    ]
    return random.choice(responses)

prompt = "Explain NLP in simple words"
output = gpt3_mock(prompt)

print("Prompt:", prompt)
print("Generated Text:", output)
