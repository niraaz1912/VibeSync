from transformers import pipeline

# Load the emotion classification model from Hugging Face
emotion_analyzer = pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base')

# Text to analyze
text = "I am so happy today, everything is going perfectly!"

# Get emotion classification result
result = emotion_analyzer(text)

# Print the result
print(result)