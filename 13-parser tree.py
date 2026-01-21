from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'She'
VP -> V NP
V -> 'loves'
NP -> 'Python'
""")

parser = ChartParser(grammar)
sentence = ['She', 'loves', 'Python']

for tree in parser.parse(sentence):
    tree.pretty_print()
