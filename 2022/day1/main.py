import numpy as np

def parse_list(arr):
  res = 0
  all_res = []
  last = 0
  for value in arr:
    if value == "\n": 
      all_res.append(last)
      last = 0
    else :
      value = int(value)
      last += value
  all_res.append(last)
  return all_res


def exo1(arr):
  all_res = parse_list(arr)
  res = max(all_res)
  print("exo 1 : ", res)

def exo2(arr):
  res = 0
  all_res = parse_list(arr)
  all_res.sort(reverse=True)

  res = sum(all_res[0:3])

  print("exo 2 : ", res)


if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()

    exo1(arr)
    exo2(arr)
