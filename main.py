from csv import reader
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--rule', help='rules for the morphology')
parser.add_argument('--document', help='The document to translate')
args = parser.parse_args()


def read_rules():
    with open(args.rule or 'test/rules.csv', 'r') as f:
        csv_reader = reader(f)
        rules = {line[0]: line[1] for line in csv_reader}
    return rules


def read_document():
    with open(args.document or 'test/original.txt', 'r') as f:
        document = f.read()
    return document


def capitalize(sentence):
    return sentence[0].upper() + sentence[1:]


def split_word(word):
    morphemes = word.split('.')
    if len(morphemes) > 0 and len(morphemes[-1]) > 0 and morphemes[-1][-1] in [',', '?', ';', ':', '!']:
        punctuation = morphemes[-1][-1]
        morphemes[-1] = morphemes[-1][:-1]
        morphemes.append(punctuation)
    return morphemes


def translate_sentence(sentence, rules):
    return ' '.join([
        ''.join([
            rules[morpheme] if morpheme in rules else morpheme
            for morpheme in split_word(word)
        ]) for word in sentence.split(' ')
    ])


def translate(document, rules):
    return '.\n'.join([
        '. '.join([
            capitalize(translate_sentence(sentence, rules))
            for sentence in paragraph.split('. ')
        ]) for paragraph in document.split('.\n')
    ])


if __name__ == "__main__":
    document = read_document()
    rules = read_rules()
    print(translate(document, rules))
