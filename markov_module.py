import random


class MarkovChain(object):
    def __init__(self, list_words):
        self.dict = {}
        self.words = list_words
        self.words_size = len(self.words)
        self.markov_model()

    def markov_triples(self):
        if len(self.words) < 3:
            return
        for i in range(len(self.words) - 2):
            yield(self.words[i], self.words[i+1], self.words[i+2])

    def markov_model(self):
        for word1, word2, word3 in self.markov_triples():
            dict_key = (word1, word2)
            if dict_key in self.dict:
                self.dict[dict_key].append(word3)
            else:
                self.dict[dict_key] = [word3]

    def generate_sentence(self, size=25):
        first_index = random.randint(0, self.words_size-3)
        first_word, second_word = self.words[first_index], self.words[first_index+1]
        word1, word2 = first_word, second_word
        sentence_words = []
        for i in range(size):
            sentence_words.append(word1)
            word1, word2 = word2, random.choice(self.dict[(word1, word2)])
        sentence_words.append(word2)
        return ' '.join(sentence_words)


if __name__ == '__main__':
    import sys
    source = open(sys.argv[1]).read()
    tokens = tokenize(source)
    markov = MarkovChain(tokens)
    sentence = markov.generate_sentence(50)
    print(sentence)
