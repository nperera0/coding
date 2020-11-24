a = [4, 6, 3,3,3,3,9]


mapping = { 2:['A','B','C'], 3: ['D','E','F'], 9:['W','X', 'Y', 'Z'] }


def rec_function( letters , numbers):
  if numbers == []:
      print(''.join(letters))
      return

  digit = numbers[0]

  #print(mapping[digit][0])

  #print(letters)
  #print(numbers)

  l1 = letters[:]
  l2 = letters[:]
  l3 = letters[:]
  l1.append(mapping[digit][0])
  l2.append(mapping[digit][1])
  l3.append(mapping[digit][2])

  #print(l1)
  #print(l2)
  #print(l3)

  if digit == 7 or digit == 9:
      l4 = letters[:]
      l4.append(mapping[digit][3])

      #print(l4)

      rec_function(l1, numbers[1:])
      rec_function(l2, numbers[1:])
      rec_function(l3, numbers[1:])
      rec_function(l4, numbers[1:])

  else:
      rec_function(l1, numbers[1:])
      rec_function(l2, numbers[1:])
      rec_function(l3, numbers[1:])


rec_function([], [2,9,3])
