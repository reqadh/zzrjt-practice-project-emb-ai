import unittest

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        l_1 = sentiment_analyzer('I love python')
        self.assertEqual(l_1['label'], 'SENT_POSITIVE')
        l_2 = sentiment_analyzer('I Python')
        self.assertEqual(l_2['label'], 'SENT_NEGATIVE')
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')