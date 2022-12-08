def exo1(arr):
  for value in arr:
    print (value)
  res = 0
  return res

def exo2(arr):
  res = 0
  return res

def parse_data(data):
  data_arr = data.readlines()
  return [value.strip() for value in data_arr]

def solve(data, example, sol1, sol2 = None):
  data = parse_data(data)
  print("# Step 1")

  res1 = exo1(example)
  print("  Example:", res1)
  if res1 == sol1:
    print("  Data:", exo1(data))

  print("\n# Step 2")
  res1 = exo2(example)
  print("  Example:", res1)
  if res1 == sol2:
    print("  Data:", exo2(data))

if __name__ == "__main__":
  with open("example.txt","r") as example:
    with open("data.txt","r") as data:
      solve(data, example, 2)