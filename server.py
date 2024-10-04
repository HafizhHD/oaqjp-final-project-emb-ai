"""Function printing python version."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion")


@app.route("/emotionDetector")
def emot_detector():
    """Function printing python version."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response["score"]["anger"]
    disgust = response["score"]["disgust"]
    fear = response["score"]["fear"]
    joy = response["score"]["joy"]
    sadness = response["score"]["sadness"]
    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger':"
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """Function printing python version."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    