import collections

with open('bbc_news_headlines.txt', 'r') as f:
    text = f.read()

words = text.split()

word_counts = collections.Counter(word for word in words if len(word) > 3)

for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")
