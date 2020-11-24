def reverse_words(sentence):    # sentence here is an array of characters

  word_list = sentence.split()
  rev = word_list[::-1]
  ret = ' '.join(rev)

  return ret

print(reverse_words('We love Python'))
