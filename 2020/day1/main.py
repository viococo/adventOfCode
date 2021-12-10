def metho1(arr):
  res = []
  for index1, value in enumerate(arr):
    value = int(value)
    print (value)
    for index2, add in enumerate(arr):
      add = int(add)

      if index1 == index2:
        continue
      if value + add == 2020:
        res.append(value)
        res.append(add)
        break
    if len(res) > 0:
      break

  print("metho 1", res[0]*res[-1])
  # 987339

def addTo2020(arr, maxDepth, resArr = []):
  for index, value in enumerate(arr):
    value = int(value)
    resArr.append(value)

    if maxDepth == len(resArr):
      add = reduce(lambda a,b: a + b, resArr)
      print( "on y croit", resArr, add)
      if add == 2020:
        return resArr
      return 
    
    return addTo2020(arr, maxDepth, resArr)



def exo1(arr):
  addTo2020(arr, 2)
  

def exo2(arr):

  print("exo 2", )


if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()

    exo1(arr)
    exo2(arr)
