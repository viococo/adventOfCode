import copy

def get_marker(value, size):
  for index in range(len(value)):
    marker = value[index:index + size]
    if len(set(marker)) == size:
      return index + size

def exo1(arr):
  value = arr[0]

  size = 4
  return get_marker(value, size)

def exo2(arr):
  value = arr[0]

  size = 14
  return get_marker(value, size)

def parse_data(data):
  data_arr = data.readlines()
  data_arr = [value.replace("\n","") for value in data_arr]

  return data_arr

def solve(data, example, sol1, sol2 = None):
  example = parse_data(example)
  data = parse_data(data)

  print("\n# Step 1")
  res1 = exo1(copy.deepcopy(example))
  print("  Example:", res1)
  if res1 == sol1:
    print("  Data:", exo1(copy.deepcopy(data)))

  print("\n# Step 2")
  res2 = exo2(example)
  print("  Example:", res2)
  if res2 == sol2:
    print("  Data:", exo2(data))

if __name__ == "__main__":
  with open("example.txt","r") as example:
    with open("data.txt","r") as data:
      solve(data, example, 7, 19 )