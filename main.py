from emotion_analyzer import predict_emotion
from recommendSong import get_recommendations

text = "I am feeling sad"

emotion = predict_emotion(text)

tracks = get_recommendations(emotion)

for track in tracks:
    print(track)
