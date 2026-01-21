grammar = {
    'S': [['NP','VP']],
    'NP': [['I']],
    'VP': [['run']]
}

def parse(symbols, sentence):
    if not symbols and not sentence:
        return True
    if not symbols:
        return False
    first, rest = symbols[0], symbols[1:]
    if first in grammar:
        for prod in grammar[first]:
            if parse(prod + rest, sentence):
                return True
    else:
        if sentence and first == sentence[0]:
            return parse(rest, sentence[1:])
    return False

print(parse(['S'], ['I','run']))
