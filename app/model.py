import random

class SimpleTextGenerator:
    def __init__(self, corpus):
        self.model = self.build_model(corpus)

    def build_model(self, text):
        words = text.split()
        model = {}
        for i in range(len(words)-1):
            key = words[i]
            next_word = words[i+1]
            model.setdefault(key, []).append(next_word)
        return model

    def generate(self, start_word, length=10):
        word = start_word
        result = [word]
        for _ in range(length-1):
            next_words = self.model.get(word)
            if not next_words:
                break
            word = random.choice(next_words)
            result.append(word)
        return ' '.join(result)
