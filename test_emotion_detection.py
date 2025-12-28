"""test_emotion_detection.py: egységtesztek a emotion_detector függvényhez"""

from EmotionDetection import emotion_detector

def run_tests():
    test_cases = test_cases = [
    ("I am glad this happened", "joy"),
    ("I am very angry about this", "anger"),
    ("I am disgusted just hearing about this", "disgust"),
    ("I am very sad about this", "sadness"),
    ("I am very afraid that this will happen", "fear"),
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