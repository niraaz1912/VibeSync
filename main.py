from emotion_analyzer import predict_emotion
from user_identificaiton import get_recommendations

text = "I want to listen to AC/DC song"

emotion = predict_emotion(text)
print(emotion)
tracks = get_recommendations(emotion)

for track in tracks:
    print(track)
