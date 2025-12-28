"""test_emotion_detection.py: egységtesztek a emotion_detector függvényhez"""

from Final_project_flask.EmotionDetection.emotion_detection import emotion_detector

def run_tests():
    test_cases = [
        ("Örülök, hogy ez történt", "joy"),
        ("Nagyon dühös vagyok emiatt", "anger"),
        ("Már attól is undorodom, hogy hallok erről", "disgust"),
        ("Nagyon szomorú vagyok emiatt", "sadness"),
        ("Nagyon félek, hogy ez meg fog történni", "fear"),
    ]

    for text, expected in test_cases:
        result = emotion_detector(text)

        assert isinstance(result, dict), f"Expected dict, got {type(result)}"
        assert "dominant_emotion" in result, "Missing key: dominant_emotion"
        assert result["dominant_emotion"] == expected, (
            f"Text: {text}\nExpected: {expected}\nGot: {result['dominant_emotion']}\nFull result: {result}"
        )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()