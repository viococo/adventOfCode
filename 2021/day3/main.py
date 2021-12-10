
def count(arr):
  count0 = arr.count('0')
  count1 = arr.count('1')

  return count0, count1


def getArrByBit(arr):
  arrToUse = []
  for binary in arr:
    for depth, number in enumerate(binary):
      if len(arrToUse) <= depth:
        arrToUse.append([])
      arrToUse[depth].append(number)
  arrToUse = arrToUse[:-1]
  return arrToUse

def countNew(arr, orders):
  res = []
  for txt in orders:
    res.append(arr.count(txt))
  return res


def exo1(arr):
  epsilon = 0

  arrToUse = getArrByBit(arr)

  gammaArr = []
  epsilonArr = []
  for line in arrToUse:
    count0, count1 = count(line)

    if count1 > count0:
      gammaArr.append("1") 
      epsilonArr.append("0") 
    else:
      gammaArr.append("0")
      epsilonArr.append("1")

  gamma = int("".join(gammaArr), 2)
  epsilon = int("".join(epsilonArr), 2)
  print("exo1", gamma * epsilon )


def getBitArrByDepth(arr, depth):
  res = []
  for number in arr:
      res.append(number[depth])
  return res

def findBinary(arr, order):
  depthMax = len(arr[0]) - 1
  
  arrFiltered = arr
  for depth in range(depthMax):
    line = getBitArrByDepth(arrFiltered, depth)
    count0, count1 = count(line)
    if count0 > count1:
      arrFiltered = filter(lambda x: x[depth] == order[0], arrFiltered)
    else:
      arrFiltered = filter(lambda x: x[depth] == order[-1], arrFiltered)
    
    if len(arrFiltered) == 1:
      binary = arrFiltered[0]
      return int(binary, 2)

def exo2(arr):
  oxygene = findBinary(arr, ["0", "1"])
  c02 = findBinary(arr, ["1", "0"])
  print("exo2",oxygene*c02)


if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()

    exo1(arr)
    exo2(arr)
