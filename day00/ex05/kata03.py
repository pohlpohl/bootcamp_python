phrase = "The right format"

if 42 - len(phrase) > 0:
    print('-' * (42 - len(phrase) - 1) + phrase)
else:
    print(phrase)
