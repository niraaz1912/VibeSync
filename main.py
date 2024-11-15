from emotion_analyzer import predict_emotion
from user_identificaiton import recommend

text = "I am the sad."

emotion = predict_emotion(text)
print(emotion)
tracks = recommend(emotion)

for track in tracks:
    print(track)
