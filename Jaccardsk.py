from sklearn.metrics import jaccard_score

line_1 = "I love ice-cream and cheese most times"
line_2 = "I hate cheesecake and blue cheese but love all ice-cream"

# Create two sets with unique words
str_line_1 = set(line_1.split())
str_line_2 = set(line_2.split())


all_words = str_line_1.union(str_line_2)
a = [1 if w in str_line_1 else 0 for w in all_words]
b = [1 if w in str_line_2 else 0 for w in all_words]

print("Words only in line 1", a)
print("Words only in line 2", b)

print(jaccard_score(a, b))
