import re

text = input("Enter a text: ")

cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())
words = cleaned_text.split()

word_counts = {}
for word in words:
    if word:
        word_counts[word] = word_counts.get(word, 0) + 1

similar_words = {word: count for word, count in word_counts.items() if count > 1}

print("Repeated words:")
for word, count in sorted(similar_words.items()):
    print(f"{word}: {count} times")

print(f"Number of similar words: {len(similar_words)}")
