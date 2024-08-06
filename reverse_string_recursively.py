def reverse_string(word):
  if len(word) == 0:
    return word
  return  reverse_string(word[1:]) + word[0]

print(reverse_string('Python'))