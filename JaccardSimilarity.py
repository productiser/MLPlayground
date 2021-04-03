line_1 = "I love ice-cream and cheese most times"
line_2 = "I hate cheesecake and blue cheese but love all ice-cream"

# Create two sets with unique words
str_line_1 = set(line_1.split())
str_line_2 = set(line_2.split())

# Get count of each line of unique words
uniq_words_line1 = len(str_line_1)
uniq_words_line2 = len(str_line_2)

# find common words in both lines using intersection and their count
common_words = str_line_1.intersection(str_line_2)
count_common_words = len(common_words)

# get lisst of all words in both ssets using uniq_words_line1
all_words = str_line_1.union(str_line_2)
count_all_words = len(all_words)

# Jaccard similarity

similarity = count_common_words / (1.0 * count_all_words)

# print
print("No. of words in line 1 = %d" % (uniq_words_line1))
print("line 1 words =", line_1)
print("No. of words in line 2 = %d" % (uniq_words_line2))
print("line 1 words =", line_2)
print("Number of words in common = %d" % (count_common_words))
print("Common words", common_words)
print("Number of unique words = %d" % (count_all_words))
print("All words", all_words)
print("-----------------------")
print("similarity = num common words / num of unique words %d/%d = %.2f"
    % (count_common_words, count_all_words, similarity))
