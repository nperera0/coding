''''
Given an array of words, find all possible 2-word pairs, where the words are adjacent.
For eg. if input is "My name is Leo", output should be: [[My, name], [name, is], [is, Leo]].
'''

def nWordPairs(text, n=2):
    output = []
    pair = []
    words = text.split(" ")
    for word in words:
        pair.append(word)

        if len(pair) == n:
            output.append(pair)
            pair = []
            pair.append(word)
    return output


results = nWordPairs("My name is Leo")
print(results) # [[My, name], [name, is], [is, Leo]]

results = nWordPairs("My name is Nisal Perera")
print(results) # [[My, name], [name, is], [is, Leo]]


results = nWordPairs("My name is Nisal Perera", 3)
print(results) # [[My, name, is], [is, Nisal, Perera]]
