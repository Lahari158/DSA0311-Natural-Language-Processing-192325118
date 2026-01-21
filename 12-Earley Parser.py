import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'I'
VP -> 'run'
""")

parser = EarleyChartParser(grammar)

for tree in parser.parse(['I','run']):
    tree.pretty_print()
