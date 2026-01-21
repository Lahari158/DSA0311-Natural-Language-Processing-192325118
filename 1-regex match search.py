import re

text = "My email is example@test.com"
pattern = r'\w+@\w+\.\w+'

match = re.search(pattern, text)
if match:
    print("Found:", match.group())
