import re


def tokenize(text):
    no_punc_text = remove_punctuation(text)
    tokens = split_n_clean(no_punc_text)
    tokens.remove('')
    tokens = lower_case(tokens)
    return tokens


def lower_case(tokens):
    words = ['Apple', 'Macintosh', 'IBM', 'Lisa', 'Windows', 'Microsoft', 'Macworld', 'Mac', 'iPod', 'iPhone', 'TV', 'Jony', 'Ive', 'Steve']
    tokens = [x.lower() if (x not in words) else x for x in tokens]
    return tokens


def split_n_clean(text):
    text = re.sub('(\[[^\]]*\])', '', text)
    return re.split('\s+', text)


def remove_punctuation(text):
    no_punc_text = re.sub('[,()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text


if __name__ == '__main__':
    import sys
    source = open(sys.argv[1]).read()
    tokens = tokenize(source)
    print(tokens)
    print(len(tokens))
