from emotion_analyzer import predict_emotion
from user_identificaiton import get_recommendations

text = "The news about the sudden passing of my childhood friend hit me like a wave, and I can hardly process how to cope with this deep sense of loss and grief."

emotion = predict_emotion(text)
print(emotion)
tracks = get_recommendations(emotion)

for track in tracks:
    print(track)
