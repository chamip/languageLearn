class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def letter_count(self):
        return len(self.sentence)

    def word_count(self):
        return len(self.sentence.split(" "))

    def upper_alpha_count(self):
        cnt = 0
        for a in self.sentence:
            if a >= "A" and a <= "Z":
                cnt += 1
        return cnt