from collections import defaultdict, Counter

sentence = "Peter Piper picked a peck of pickled peppers\
A peck of pickled peppers Peter Piper picked\
If Peter Piper picked a peck of pickled peppers\
Whereas the peck of pickled peppers Peter Piper picked"

word_dict = defaultdict(int)

for word in sentence.split():
    word_dict[word] += 1

print(word_dict)
for key, value in word_dict.items():
    print(key, value)

word_count = Counter(sentence.split())
print(word_count)
