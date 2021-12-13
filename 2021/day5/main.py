def calcIndexes(value, lengthX, lengthY):
  startX = value.get("startX")
  endX = value.get("endX")
  startY = value.get("startY")
  endY = value.get("endY")

  indexes = []

  if startX == endX:
    for y in range(startY, endY + 1):
      index = startX + (y * lengthX)
      indexes.append(index)
  elif startY == endY:
    for x in range(startX, endX + 1):
      index = x + (startY * lengthX)
      indexes.append(index)

  return indexes


def logData(data, lengthX, lengthY):
  for y in range(lengthY):
    cells = []
    for x in range(lengthX):
      index = x+(y * lengthX)
      cells.append(data[index])
    print(cells)
  print("")

def exo1(arr):
  lengthX, lengthY = findLength(arr)
  maxIndexes = (lengthX) * (lengthY)
  res = [0] * maxIndexes

  print("maxIndexes",maxIndexes)

  for value in arr:
    indexes = calcIndexes(value, lengthX, lengthY)
    for index in indexes:
      res[index] += 1

  logData(res, lengthX,lengthY)
  print(">> exo 1", sum(1 for i in res if i > 1))




def exo2(arr):
  res = 0
  print("exo 2", res)

def parseData(arr):
  res = []

  for value in arr:
    first, last = value.split(" -> ")
    firstX, firstY = first.split(",")
    lastX, lastY = last.replace("\n", "").split(",")

    startX = min(int(firstX), int(lastX))
    startY = min(int(firstY), int(lastY))
    
    endX = max(int(firstX), int(lastX))
    endY = max(int(firstY), int(lastY))

    res.append({"startX":int(startX), "startY":int(startY), "endX":int(endX), "endY":int(endY)})

  return res

def findLength(data):
  allX = []
  allY = []
  for value in data:
    allX.append(value.get("startX"))
    allX.append(value.get("endX"))

    allY.append(value.get("startY"))
    allY.append(value.get("endY"))

  lengthX = max(allX) + 1
  lengthY = max(allY) + 1

  return lengthX, lengthY



if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()
    data = parseData(arr)


    exo1(data)
    # exo2(data)
