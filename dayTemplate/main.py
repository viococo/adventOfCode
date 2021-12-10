def exo1(arr):
  for value in arr:
    print (value)
  res = 0
  print("exo 1", res)

def exo2(arr):
  res = 0
  print("exo 2", res)


if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()

    exo1(arr)
    exo2(arr)
