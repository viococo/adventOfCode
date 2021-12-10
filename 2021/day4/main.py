BOARD_WIDTH = 5

def parseBoards(boards):
  boards = boards.read().split('\n\n')
  boardsRes = []
  for board in boards:
    board = board.replace('\n', " ")
    board = board.split(" ")
    board = filter(lambda x: not(x == ""), board)

    res = []
    for number in board:
      res.append([number, False])
    boardsRes.append(res)

  return boardsRes

def checkRow(board):
  for x in range(BOARD_WIDTH):
    isChecked = []
    for y in range(BOARD_WIDTH):
      index = BOARD_WIDTH * x + y
      case = board[index]
      if case[1]:
        isChecked.append(case[0])
    if(len(isChecked) == BOARD_WIDTH):
      return True
  return False

def checkColumn(board):
  for y in range(BOARD_WIDTH):
    isChecked = []
    for x in range(BOARD_WIDTH):
      index = BOARD_WIDTH * x + y
      case = board[index]
      if case[1]:
        isChecked.append(case[0])
    if(len(isChecked) == BOARD_WIDTH):
      return True
  return False

def checked(draw, board):
  for index, case in enumerate(board):
    number = case[0]
    if(case[0] == draw):
      board[index] = [number, True]

def calcRes(draw, board):
  print(draw,board)
  res = 0
  for case in board:
    if(not(case[1])):
      res += int(case[0])
  return res * int(draw)

def exo1(boards, draws):
  for draw in draws:
    isWon = False

    for board in boards:
      checked(draw, board)
      isWon = checkColumn(board) or checkRow(board)
      if isWon:
        print(calcRes(draw, board))
        return

def exo2(boards, draws):
  countBoards = len(boards)
  indexBoardsWhoWin = []
  finalDraw = 0
  for draw in (draws):
    for index, board in enumerate(boards):
      if not(index in indexBoardsWhoWin):
        checked(draw, board)
        if checkColumn(board) or checkRow(board):
          indexBoardsWhoWin.append(index)
          if len(indexBoardsWhoWin) == countBoards:
            finalDraw = draw
            print(calcRes(draw, board))
            return 


if __name__ == "__main__":
  with open("boards.txt","r") as boards:
    with open("draws.txt","r") as draws:
      boards = parseBoards(boards)
      draws = draws.readline().split(',')

      exo1(boards, draws)
      exo2(boards, draws)
