import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """survey.py单元测试"""

    def setUp(self):
        """创建一个调查对象（一个问题）和一组答案"""
        question = 'What language did you learn to speak?'
        self.my_servey = AnonymousSurvey(question)
        self.responses = ['Chinese', 'English', 'Japanese']

    def test_single_response(self):
        """测试单个答案"""
        self.my_servey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_servey.responses)

    def test_three_responses(self):
        """测试三个答案的情况"""
        for response in self.responses:
            self.my_servey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_servey.responses)

unittest.main()
