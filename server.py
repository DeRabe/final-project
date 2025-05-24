"""
Flask Webserver for Emotion Detection project.
Provides a web interface for analyzing emotional tone of text input.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the main web interface.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Receives user input, performs emotion detection,
    and returns a formatted summary or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    if isinstance(result, dict) and "dominant_emotion" in result:
        response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    else:
        response = "Invalid input or analysis failed."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    