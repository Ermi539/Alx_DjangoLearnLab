def find(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1

def find_word(sentence, keyword):
    words = sentence.split()
    return find(words, keyword)

# Test cases
print(find_word('paramount sees green in the red', 'paramount'))  # should return 0
print(find_word('paramount sees green in the red', 'para'))        # should return -1
