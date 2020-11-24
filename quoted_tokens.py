'''
You are given a string containing a comma-separated list of
tokens. Tokens may have zero length, contain internal commas,
or be surrounded by double quotes ("). Write a function that
parses the string character-by-character and returns a list
of tokens, preserving any quoted tokens.

Notes:
- All input will be well-formed.
- Quote characters will never appear internally within tokens.
- Quote characters should not appear in the final output.

Examples:
1) parse('apple,banana') = ['apple', 'banana']
2) parse('"a",b,"c,d"') = ['a', 'b', 'c,d']
3) parse(',,') = ['', '', '']
4) parse('') = ['']

'''


def parse(string):

    output  = []
    inQuotes = False
    buffer = ''

    for char in string:
        if char == '"':
            inQuotes = not inQuotes
        elif char == ',' and not inQuotes:
            output.append(buffer)
            buffer = ''
        else:
            buffer = buffer + char

    output.append(buffer)
    return output


print(parse('apple,banana')) #== ['apple', 'banana'])
print(parse('"a",b,"c,d"')) #== ['a', 'b', 'c,d'])
print(parse(',,')) #== ['', '', ''])
print(parse('')) #== [''])
