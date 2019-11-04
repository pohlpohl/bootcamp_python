languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

l = list(languages.keys())

for i in range(len(languages)):
    print(l[i] + " was created by " + languages[l[i]])
