from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="SamLowe/roberta-base-go_emotions")

result = classifier("I got a new job")
print(result)
