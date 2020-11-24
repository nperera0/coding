'''
Write a function that returns whether a list of strings is sorted given a specific alphabet.
A list of N words and the K-sized alphabet are given.

input:  words =    [ "cat", "catt",  "cbt", "bat", "tab"]
        alphabet = ['c', 'b', 'a', 't']
output: True

'''

def sortedWords(words, alphabet):

    if len(words) <= 1:
        return True

    if len(alphabet) == 0:
        return True

    prevWord = words[0]


    for index in range(1: len(words)- 2):
        curWord = words[index]

        for position, character in enumerate(prevWord):

            if position > len(curWord) -1:
                return False

            if character not in alphabet:
                return False

            if alphabet.index(character) < alphabet.index(prevWord[position]:
                return False

            if alphabet.index(character) > alphabet.index(prevWord[position]:
                break

       prevWord = curWord


    return True


# tests

words =    ["cat", "cbt", "bat", "tab"]
alphabet = ['c', 'b', 'a', 't']


print(sortedWords(words, alphabet)) #False




'''
Given a string with alpha-numeric characters and parentheses, return a string with balanced parentheses by removing the fewest characters possible. You cannot add anything to the string.
Balanced parentheses means that each opening parenthesis has a corresponding closing parenthesis and the pairs of parentheses are properly nested.


'aaa(bb)c(aa)aa(a'
'aaa(bb)c(aa)aaa'

'''

[('(', 9) ]

def replaceParentheses( string):


    stack = []
    for index, char in enumerate(string):

        if char == '(':
            stack.append(('(', index))

        if char == ')':
            if stack[len(stack)][0] == '(':
                stack.pop(len(stack))
