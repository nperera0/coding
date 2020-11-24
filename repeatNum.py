
'''
 Find the non repeated number in an array
'''
arr = [1, 5, 8, 1, 8]
result = 0
for num in arr:
  result ^= num
  print(result)
