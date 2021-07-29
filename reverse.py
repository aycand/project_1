arr = [[1, 2], [3, 4], [5, 6, 7]]

def reverser(inputList):
  inputList.reverse()
  for item in inputList:
    if type(item) == list:
      reverser(item)
  return inputList

print(reverser(arr))

