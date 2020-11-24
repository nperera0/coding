'''
String segmentation
You are given a dictionary of words and a large input string.
You have to find out whether the input string can be completely segmented into the words of a given dictionary.
The following two examples elaborate on the problem further.

Given a dictionary of words.

apple
apple
pear
pie
Input string of “applepie” can be segmented into dictionary words.

apple
pie
Input string “applepeer” cannot be segmented into dictionary words.

apple
peer
'''

def can_segment_string(s, dictionary):
  map = dict()
  return can_segment_string_helper(s, dictionary, map)

def can_segment_string_helper(s, dictionary, map):
  if s == '':
    return True

  if s in map:
    return map[s]

  for i in range(len(s)+1):
    if s[0:i] in dictionary and can_segment_string(s[i:len(s)], dictionary):
      map[s[i:len(s)]] = True
      return True

  map[s] = False
  return False
