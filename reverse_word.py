x = 'My name is Michele'
def reverse_v1(x):
  y = x.split()         # y=['My', 'name', 'is', 'Michele']
  result = []
  for word in y:
    result.insert(0,word)  #insert object in 0th position every time
  return " ".join(result)

print (reverse_v1(x))
