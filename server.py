"""server.py: a flask szerver az emotion detection apphez"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Kirajzolja a főoldalt."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """Extract the text to analyze from the Flask request."""
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze is None:
        text_to_analyze = request.form.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)


    if result.get("dominant_emotion") is None:
        return "Érvénytelen szöveg! Kérlek, próbáld újra!."

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        "A megadott kijelentésre a rendszer válasza: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} és 'sadness': {sadness}. "
        f"A domináló érzelem: {dominant}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
