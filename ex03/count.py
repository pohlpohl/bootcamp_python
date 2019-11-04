import string

def text_analyser(text = 0):
    """Counts the characters of a string depending on their type"""
    if (not text):
        text = input("What is the text to analyse?\n>> ")
    print("The text contains " + str(len(text)) + " characters:")
    if sum(1 for c in text if c.isupper()) :
        print("- " + str(sum(1 for c in text if c.isupper())) + " upper letters")
    if sum(1 for c in text if c.islower()) :
        print("- " + str(sum(1 for c in text if c.islower())) + " lower letters")
    punc_count = sum(1 for c in text if c in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"))
    if punc_count:
        print("- " + str(punc_count) + " punctuation marks")
    if text.count(' '):
        print("- " + str(text.count(' ')) + " spaces")
