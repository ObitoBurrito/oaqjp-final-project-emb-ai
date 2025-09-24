import requests
import json

def emotion_detector(text_to_analyze):
    # Blank input → return None values (required by Task 7)
    if not text_to_analyze or not str(text_to_analyze).strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        resp = requests.post(url, json=payload, headers=headers)
    except Exception:
        # Network or unexpected error → treat as invalid input
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # API signals bad request (e.g., empty text) → return None values
    if resp.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    data = json.loads(resp.text)
    scores = data["emotionPredictions"][0]["emotion"]

    result = {
        "anger": float(scores.get("anger", 0.0)),
        "disgust": float(scores.get("disgust", 0.0)),
        "fear": float(scores.get("fear", 0.0)),
        "joy": float(scores.get("joy", 0.0)),
        "sadness": float(scores.get("sadness", 0.0)),
    }
    result["dominant_emotion"] = max(result, key=result.get)
    return result
