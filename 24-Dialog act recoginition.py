def dialog_act(sentence):
    sentence = sentence.lower()
    if sentence.endswith("?"):
        return "Question"
    elif "please" in sentence:
        return "Request"
    elif sentence.startswith("thank"):
        return "Thanking"
    else:
        return "Statement"

dialog = [
    "Can you help me?",
    "Please open the door",
    "Thank you",
    "I am learning NLP"
]

for d in dialog:
    print(d, "->", dialog_act(d))
