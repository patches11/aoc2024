
directs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
import copy

def char_to_dir(char):
  if char == "^":
    return (0, -1)
  if char == "v":
    return (0, 1)
  if char == "<":
    return (-1, 0)
  if char == ">":
    return (1, 0)
  else:
    return None

def move(pos, direct, arr, force_turn=False):
  new_pos = pos[0] + direct[0], pos[1] + direct[1]
  new_direct = direct
  x, y = new_pos
  if force_turn or arr[y][x] == "#":
    new_pos = pos
    new_direct = directs[(directs.index(direct) + 1) % len(directs)]
  return new_pos, new_direct

# 4721 too low
def p1():
  arr = []
  with open("input.txt", "r") as file:
      for line in file:
        arr.append(list(line.strip()))

  for y in range(len(arr)):
    for x in range(len(arr[0])):
      tmp_direct = char_to_dir(arr[y][x])
      if tmp_direct is not None:
        pos = (x, y)
        direc = tmp_direct

  uniques = set()

  oob = False
  uniques.add(pos)
  while not oob:
    try:
      pos, direc = move(pos, direc, arr)
      uniques.add(pos)
    except IndexError:
      oob = True

  print(len(uniques))
  
def test_turn(pos, direc, arr):
  new_route = set()
  new_arr = copy.deepcopy(arr)
  next_x, next_y = (pos[0] + direc[0], pos[1] + direc[1])
  new_arr[next_y][next_x] = "#"

  try:
    while True:
      pos, direc = move(pos, direc, new_arr)
      if (pos, direc) in new_route:
        return True
      new_route.add((pos, direc))
  except IndexError:
    return False

def p2():
  arr = []
  with open("input.txt", "r") as file:
      for line in file:
        arr.append(list(line.strip()))

  for y in range(len(arr)):
    for x in range(len(arr[0])):
      tmp_direct = char_to_dir(arr[y][x])
      if tmp_direct is not None:
        pos = (x, y)
        direc = tmp_direct

  start_pos = pos
  start_direc = direc

  uniques = set()
  oob = False
  while not oob:
    try:
      pos, direc = move(pos, direc, arr)
      next_x, next_y = (pos[0] + direc[0], pos[1] + direc[1])
      if arr[next_y][next_x] != "#" and (next_x, next_y) != start_pos and test_turn(pos, direc, arr):
        uniques.add((next_x, next_y))
    except IndexError:
      oob = True

  #print(uniques)
  print(len(uniques))
  # 5353
  # 4859 too high
  # 1850 too high
  # 1798 too high
  # 1797 wrong


if __name__ == "__main__":
  p2()