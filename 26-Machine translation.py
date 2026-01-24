from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = "Machine learning is very interesting"
inputs = tokenizer(text, return_tensors="pt")

translated = model.generate(**inputs)
result = tokenizer.decode(translated[0], skip_special_tokens=True)

print("English :", text)
print("French  :", result)
