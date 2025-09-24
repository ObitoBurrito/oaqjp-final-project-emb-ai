import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def _check(self, text, expected):
        res = emotion_detector(text)
        self.assertEqual(res["dominant_emotion"], expected)

    def test_joy(self):
        self._check("I am glad this happened", "joy")

    def test_anger(self):
        self._check("I am really mad about this", "anger")

    def test_disgust(self):
        self._check("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        self._check("I am so sad about this", "sadness")

    def test_fear(self):
        self._check("I am really afraid that this will happen", "fear")

if __name__ == "__main__":
    unittest.main()
