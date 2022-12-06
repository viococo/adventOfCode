LETTER_TO_FIGURE = {
  "A": "rock",
  "B": "paper",
  "C": "scissors",
  "X": "rock",
  "Y": "paper",
  "Z": "scissors",
}

FIGURE_TO_POINTS = {
  "rock": 1,
  "paper": 2,
  "scissors": 3,
}

WON_FIGURE = {
  "rock" : "scissors",
  "paper" : "rock",
  "scissors" : "paper"
}

LOOSE_FIGURE = dict(zip(WON_FIGURE.values(),WON_FIGURE.keys()))

WON_LETTER = {
  "X": False,
  "Y": None,
  "Z": True,
}

def exo1(arr):
  all_res = []
  for value in arr:
    value = value.strip()
    values = value.split(" ")
    
    you = LETTER_TO_FIGURE[values[0]]
    me = LETTER_TO_FIGURE[values[1]]
    
    me_point = FIGURE_TO_POINTS[me]
    
    if you == me:
      all_res.append(me_point + 3)
    elif WON_FIGURE[me] == you:
      all_res.append(me_point + 6)
    else :
      all_res.append(me_point + 0)

  res = sum(all_res)
  print("exo 1", res)


def exo2(arr):
  all_res = []
  for value in arr:
    value = value.strip()
    values = value.split(" ")
    
    you = LETTER_TO_FIGURE[values[0]]
    won = WON_LETTER[values[1]]

    if won == None:
      me_point = FIGURE_TO_POINTS[you]
      all_res.append(me_point + 3)
    elif won:
      me_point = FIGURE_TO_POINTS[LOOSE_FIGURE[you]]
      all_res.append(me_point + 6)
    else :
      me_point = FIGURE_TO_POINTS[WON_FIGURE[you]]
      all_res.append(me_point + 0)

  res = sum(all_res)
  print("exo 2", res)


if __name__ == "__main__":
  with open("data.txt","r") as txt:
    arr = txt.readlines()

    exo1(arr)
    exo2(arr)
