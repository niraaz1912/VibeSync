from flask import Flask, request, render_template, jsonify
from emotion_analyzer import predict_emotion
from user_identificaiton import recommend

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # A simple HTML form for user input

@app.route('/get_recommendations', methods=['POST'])
def get_recs():
    text = request.form['mood']  # Get the user's mood from the form
    emotion = predict_emotion(text)  # Analyze the emotion
    tracks = recommend(emotion)
    
    return jsonify(recommendations=tracks)

if __name__ == '__main__':
    app.run(debug=True)