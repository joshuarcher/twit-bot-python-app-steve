from flask import Flask
from tokenizer import *
from markov_module import *
app = Flask(__name__)


@app.route('/')
def hello_word():
    source = open('steve.txt').read()
    tokens = tokenize(source)
    markov = MarkovChain(tokens)
    sentence = markov.generate_sentence(30)
    return sentence

if __name__ == '__main__':
    app.run()
