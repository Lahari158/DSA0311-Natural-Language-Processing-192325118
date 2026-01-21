def fsa_ab(s):
    return s.endswith('ab')

print(fsa_ab("cab"))  # True
print(fsa_ab("abc"))  # False
