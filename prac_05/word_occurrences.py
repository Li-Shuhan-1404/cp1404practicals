"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 10 minutes
Actual:   17 minutes
"""
from operator import itemgetter

WORD_TO_COUNT = {}
word_count = 0
word_length = 0

text = input("Text: ").split()

for word in text:
    word_count = text.count(word)
    WORD_TO_COUNT[word] = word_count

WORD_TO_COUNT = sorted(WORD_TO_COUNT.items(), key=itemgetter(0, 1))
WORD_TO_COUNT = dict(WORD_TO_COUNT)
word_length = max(len(word) for word in WORD_TO_COUNT.keys())

for word, count in WORD_TO_COUNT.items():
    print(f"{word:<{word_length}} : {count}")
