def match_word(words):
    counter = 0
    empty_list = []
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            counter += 1
            empty_list.append(word)
    print("List of words with first and last characters same, ", empty_list)
    return counter
count = match_word(["abc", "cde","ghi", "1221"])
print(count)
