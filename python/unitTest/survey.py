class AnonymousSurvey():
    """手机匿名调查问卷的答案"""

    def __init__(self, question):
        """初始化问题和答案列表"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问题"""
        print(self.question)

    def store_response(self, response):
        """存储答案"""
        self.responses.append(response)

    def show_results(self):
        """显示结果"""
        print('Survey results:')
        for response in self.responses:
            print('- ' + response)
