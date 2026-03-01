from EmotionDetection import emotion_detector


def test_emotion(statement, expected_emotion):
    result = emotion_detector(statement)
    detected_emotion = result['dominant_emotion']

    if detected_emotion == expected_emotion:
        print(f"PASS: '{statement}' → {detected_emotion}")
    else:
        print(f"FAIL: '{statement}' → {detected_emotion} (expected {expected_emotion})")


# Test cases
test_emotion("I am glad this happened", "joy")
test_emotion("I am really mad about this", "anger")
test_emotion("I feel disgusted just hearing about this", "disgust")
test_emotion("I am so sad about this", "sadness")
test_emotion("I am really afraid that this will happen", "fear")