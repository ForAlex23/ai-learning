import sys
from collections import Counter
text = sys.stdin.read()
text = text.lower()
clean_text = ''.join(
    char for char in text
    if char.isalpha() or char.isspace()
)
words = clean_text.split()
total_words = len(words)
print(f"Total words: {total_words}")
longest_word = max(words, key=len)
print(f"Longest word: {longest_word}")
counter = Counter(words)
for word, count in counter.most_common(5):
    print(f"{word}: {count}")
input("Press Enter to continue...")