import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)

    scores = data["emotionPredictions"][0]["emotion"]
    anger = scores.get("anger", 0.0)
    disgust = scores.get("disgust", 0.0)
    fear = scores.get("fear", 0.0)
    joy = scores.get("joy", 0.0)
    sadness = scores.get("sadness", 0.0)

    result = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": max(
            {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness},
            key=lambda k: {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness}[k]
        ),
    }
    return result
