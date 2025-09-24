"""Flask web server for the Emotion Detection app."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route() -> str:
    """Detect emotions in the provided text and return formatted results."""
    text = request.args.get("textToAnalyze") or request.args.get("text")

    if not text:
        data = request.get_json(silent=True) or {}
        text = (
            data.get("textToAnalyze")
            or data.get("text")
            or request.form.get("textToAnalyze")
            or request.form.get("text")
        )
        if not text and request.args:
            for _, value in request.args.items():
                if isinstance(value, str) and value.strip():
                    text = value
                    break

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    msg = (
        "For the given statement, the system response is "
        "'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        "'joy': {joy} and 'sadness': {sadness}. "
        "The dominant emotion is {dominant_emotion}."
    ).format(**result)

    return msg


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
