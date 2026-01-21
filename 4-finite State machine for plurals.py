def pluralize(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    else:
        return word + 's'

print(pluralize("cat"))  # cats
print(pluralize("city")) # cities
