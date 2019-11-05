languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

lang_keys = list(languages.keys())

for i in range(len(languages)):
    print(lang_keys[i] + " was created by " + languages[lang_keys[i]])
