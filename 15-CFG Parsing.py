from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'I' [1.0]
VP -> V OBJ [1.0]
V -> 'love' [1.0]
OBJ -> 'Python' [1.0]
""")

parser = ViterbiParser(grammar)

for tree in parser.parse(['I','love','Python']):
    tree.pretty_print()
