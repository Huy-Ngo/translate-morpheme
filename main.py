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


def translate_sentence(sentence, rules):
    return ' '.join([
        ''.join([
            rules[morpheme] if morpheme != '' else ''
            for morpheme in word.split('.')
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
