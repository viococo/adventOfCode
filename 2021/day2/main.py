
def exo1(arr):
  depth = 0
  horizontal = 0

  for value in arr:
    values = value.split(" ")
    direction = values[0]
    number = int(values[-1])

    if direction == "forward":
      horizontal += number
    elif direction == "down":
      depth += number
    elif direction == "up":
      depth -= number
    else:
      print(dir)
  
  print("exo1", horizontal * depth)


def exo2(arr):
  objective = 0
  depth = 0
  horizontal = 0

  for value in arr:
    values = value.split(" ")
    direction = values[0]
    number = int(values[-1])

    if direction == "forward":
      horizontal += number
      depth += objective * number
    elif direction == "down":
      objective += number
    elif direction == "up":
      objective -= number
    else:
      print(dir)
  
  print("exo2",horizontal*depth)
  


if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()

    exo1(arr)
    exo2(arr)
