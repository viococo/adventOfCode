
def exo1(arr):
  res = 0
  for index, value in enumerate(arr):
    if value > arr[index-1]:
      res += 1
  
  print(res)

def exo2(arr):
  arrToUse = []

  for index, value in enumerate(arr):
    if not(index + 3 > len(arr)) :
      arrToUse.append(int(value) + int(arr[index+1]) + int(arr[index+2]))
  
  exo1(arrToUse)
  


if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()
    exo1(arr)
    exo2(arr)

