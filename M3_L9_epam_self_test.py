# Dicts
import string

d = {
    "name": "Filip",
    "age": 32,
    "is_registered": False,
    "rate": 12.5,
    "total_score": 200,
    "linked_ids": [1, 45, 98]
}

"""for key in d.keys():
    print(key)
for value in d.values():
    print(value)
"""



def count_word_frequency(text):
    cleaner = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(cleaner).lower()

    occurences = dict()

    for word in clean_text.split():
        occurences[word] = occurences.get(word, 0) + 1

    return occurences

print(count_word_frequency('Hello world! This is a test. mic test. Hello again.'))