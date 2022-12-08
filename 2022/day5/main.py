import re
import copy

def get_first_all_elem(stacks):
  res = []
  for stack in stacks:
    if stack:
      res.append(stack.pop())
    else:
      res.append(" ")
  return "".join(res)

def pop_with_empty(data):
  arr = re.findall("\[(.*?)\]", data)
  if arr:
    return arr.pop()


def exo1(data):
  all_stacks, all_instructions = data

  res = all_stacks
  for instruction in all_instructions:
    count, start, end = instruction
    start = start - 1
    end = end - 1
    for _ in range(count):
      start_stack = all_stacks[start]
      end_stack = all_stacks[end]
      letter = None
      letter = start_stack.pop()

      end_stack.append(letter)

  return get_first_all_elem(res)

def exo2(data):
  all_stacks, all_instructions = data

  res = all_stacks
  for instruction in all_instructions:
    count, start, end = instruction
    start = start - 1
    end = end - 1
    
    start_stack = all_stacks[start]
    end_stack = all_stacks[end]
    payload = start_stack[len(start_stack) - count:]
    
    start_stack = start_stack[: len(start_stack) - count]
    all_stacks[start] = start_stack
    all_stacks[end] = end_stack + payload

  return get_first_all_elem(res)


def parse_instruction(instruction):
  _, count, _, start, _, end = instruction.split()
  return  int(count), int(start),int(end)

def chunk(value, n):
  return [value[i:i+n] for i in range(0, len(value), n)]

def parse_data(data):
  data_arr = data.readlines()
  data_arr = [value.replace("\n","") for value in data_arr]

  all_stacks = []
  all_instructions = []
  is_instruction = False
  for line in data_arr:
    if is_instruction:
      all_instructions.append(parse_instruction(line))
      continue
    if line == "":
      is_instruction = True
      continue

    line_chunks = chunk(line, 4)
    line_parsed = [pop_with_empty(chunk) for chunk in line_chunks]

    index = 0
    for value in line_parsed:
      if len(all_stacks) < index + 1:
        all_stacks.append([])
        if value :
          all_stacks[index].append(value)
      elif value:
          all_stacks[index].insert(0, value)
      index = index +1

  return all_stacks, all_instructions

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
      solve(data, example, "CMZ", "MCD")