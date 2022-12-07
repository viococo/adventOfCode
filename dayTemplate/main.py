def exo1(arr):
  for value in arr:
    print (value)
  res = 0
  return res

def exo2(arr):
  res = 0
  return res

def solve(data):
  print("  Exo 1:", exo1(data))
  print("  Exo 2:", exo2(data))

if __name__ == "__main__":
  print("Example")
  with open("example.txt","r") as example:
    example_arr = example.readlines()
    example_arr = [value.strip() for value in example_arr]
    solve(example_arr)

  print("Data")
  with open("data.txt","r") as data:
    data_arr = data.readlines()
    data_arr = [value.strip() for value in data_arr]
    solve(data_arr)