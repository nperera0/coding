'''
Write a function that returns all permutations of a given list.
'''

def perm_helper(prefix, suffix, ret):
    if suffix == "":
        ret.append(prefix)
        return

    for i in range(len(suffix)):
        perm_helper(prefix + suffix[i], suffix[0:i] + suffix[i+1::], ret)

    return ret


def permutations(s):
    ret = []
    return perm_helper("", s, ret)

out  = permutations("abcd")

for t in out:
    print(t)
