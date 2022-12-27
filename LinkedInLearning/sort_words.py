# # Python Code Challenge #3: Sort a String

# Your goal is to implement a function, `sort_words()`, that takes a string containing one or more words 
# separated by spaces as the input argument and returns a string containing those words sorted alphabetically.

# ## Example Test Output
# ```console
# >>> sort_words('banana ORANGE apple')
# 'apple banana ORANGE'
# ```


def sort_words(words):
  return ' '.join(sorted(words.split(), key=str.lower))

def sort_words1(words):
    return ' '.join(sorted(words.split(), key=str.casefold))

print(sort_words('banana ORANGE apple'))















