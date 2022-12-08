def parse_efls(value):
  elf1, elf2 = value.split(",")
  elf1_min, elf1_max = elf1.split("-")
  elf2_min, elf2_max = elf2.split("-")
  return elf1_min, elf1_max, elf2_min, elf2_max

def exo1(arr):
  res = 0
  for value in arr:
    elfs = parse_efls(value)
    elf1_min, elf1_max, elf2_min, elf2_max = [int(value) for value in elfs]

    if (elf1_min <= elf2_min and elf1_max >= elf2_max) or (elf2_min <= elf1_min and elf2_max >= elf1_max) :
      res = res + 1

  return res

def exo2(arr):
  res = 0
  for value in arr:
    elfs = parse_efls(value)
    elf1_min, elf1_max, elf2_min, elf2_max = [int(value) for value in elfs]

    if (elf2_min <= elf1_max and elf2_max >= elf1_max) or (elf1_min <= elf2_max and elf1_max >= elf2_max):
      res = res + 1
  return res

def parse_data(data):
  data_arr = data.readlines()
  return [value.strip() for value in data_arr]

def solve(data, example, sol1, sol2 = None):
  example = parse_data(example)
  data = parse_data(data)
  print("# Step 1")

  res1 = exo1(example)
  print("  Example:", res1)
  if res1 == sol1:
    print("  Data:", exo1(data))

  print("\n# Step 2")
  res2 = exo2(example)
  print("  Example:", res2)
  if res2 == sol2:
    print("  Data:", exo2(data))

if __name__ == "__main__":
  with open("example.txt","r") as example:
    with open("data.txt","r") as data:
      solve(data, example, 2, 4)
