'''
    returns most frequent number in an array of integers
'''

def most_frequent_int(array):  # O(n)
  if len(array) == 0:
    return None

  dictionary = dict()

  for element in array:
    if element in dictionary:
      dictionary[element] += 1
    else:
      dictionary[element] = 1

  return max(dictionary, key=dictionary.get)


print(most_frequent_int([1,2,3,4,5]))
