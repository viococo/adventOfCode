def letter_to_number(letter):
  if letter.isupper() :
    return ord(letter) - 38
  else :
    return ord(letter) - 96

def exo1(arr):
  arr_res = []
  for value in arr:
    bag_len = int(len(value) / 2)
    
    bag1 = value[0:bag_len]
    bag2 = value[bag_len:]

    letter = set(bag1).intersection(bag2).pop()

    number = letter_to_number(letter)
    
    arr_res.append(number)
    
  res = sum(arr_res)
  print("exo 1", res)


def exo2(bags):
  arr_res = []
  index = 0
  while index < len(bags):
    bag1 = bags[index]
    bag2 = bags[index + 1]
    bag3 = bags[index + 2]

    letter = set(bag1).intersection(bag2,bag3).pop()
    arr_res.append(letter_to_number(letter))
    index += 3
  res = sum(arr_res)
  print("exo 2", res)


if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()
    arr = [value.strip() for value in arr]

    exo1(arr)
    exo2(arr)
