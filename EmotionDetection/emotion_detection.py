import requests
import json

def emotion_detector(text_to_analyze):
    """Function printing python versionye."""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myJson = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myJson, headers = headers)
    response_data = json.loads(response.text)

    if response.status_code == 200:
        result = response_data['emotionPredictions'][0]['emotion']

        dominant_emotion = max(result, key=result.get)

        res = {
            "score": result,
            "dominant_emotion": dominant_emotion
        }
        return res

    if response.status_code == 400:
        test = {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
            }
        return {
            "score": test,
            "dominant_emotion": None,
        }

if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))