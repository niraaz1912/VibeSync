from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

def load_model(model_name: str):
    """
    Loads a pre-trained model and tokenizer from Hugging Face.

    Args:
    - model_name (str): Name or path of the pre-trained model.

    Returns:
    - model: Pre-trained model
    - tokenizer: Tokenizer for the pre-trained model
    """
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def preprocess_text(text: str, tokenizer):
    """
    Prepares input text for the model by tokenizing it.

    Args:
    - text (str): Input text to be processed.
    - tokenizer: The tokenizer corresponding to the model.

    Returns:
    - inputs: Tokenized and formatted inputs for the model.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    return inputs

def classify_emotion(model, inputs):
    """
    Classifies the emotion of a given text using the pre-trained model.

    Args:
    - model: The pre-trained model used for inference.
    - inputs: Tokenized and preprocessed input text.

    Returns:
    - predicted_emotion (str): The predicted emotion label.
    """
    with torch.no_grad():
        outputs = model(**inputs)  # Feed the tokenized input into the model
    
    logits = outputs.logits  # Get raw model output (logits)
    predicted_class_id = torch.argmax(logits, dim=1).item()  # Get the index of the highest logit value
    
    # Emotion labels based on model's training
    emotion_labels = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]  # Adjust according to model's training
    predicted_emotion = emotion_labels[predicted_class_id]  # Get the emotion corresponding to the predicted class ID
    
    return predicted_emotion


def predict_emotion(text: str, model_name: str = "j-hartmann/emotion-english-distilroberta-base"):
    """
    Predicts the emotion of a given text using a pre-trained model.

    Args:
    - text (str): Input text for emotion classification.
    - model_name (str): Name of the pre-trained model to use.

    Returns:
    - predicted_emotion (str): The predicted emotion.
    """
    model, tokenizer = load_model(model_name)  # Load the model and tokenizer
    inputs = preprocess_text(text, tokenizer)  # Preprocess the text
    predicted_emotion = classify_emotion(model, inputs)  # Get the predicted emotion
    return predicted_emotion


#text = ""
#predicted_emotion = predict_emotion(text)
#print(f"Predicted emotion: {predicted_emotion}")