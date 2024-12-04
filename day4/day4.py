import re

def move(location, direction):
  return location[0] + direction[0], location[1] + direction[1]

def check_direction(direction, start, arr):
  letters = ["M", "A", "S"]
  current = start
  i = 0
  for letter in letters:
    current = move(current, direction)
    try:
      x, y = current
      item = arr[y][x]
      if item != letter or x < 0 or y < 0:
        return False
      else:
        i += 1
    except:
      return False
  print(f"match {start} {direction}")
  return True


def p1():

  directions = []

  for x in range(-1, 2):
    for y in range(-1, 2):
      if not (x == 0 and y == 0):
        directions.append((x, y))

  arr = []
  with open("input.txt", "r") as file:
    for line in file:
      curr = []
      for item in line.strip():
        curr.append(item)
      arr.append(curr)

  starts = []
  for y, line in enumerate(arr):
    for x, item in enumerate(line):
      if item == "X":
        starts.append((x, y))

  count = 0
  for start in starts:
    for direction in directions:
      if check_direction(direction, start, arr):
        count += 1

  print(count)

def check_directions_2(directions, start, arr):
  nextt = None

  for direction in directions:
    current = move(start, direction)
    x, y = current
    if x < 0 or y < 0 or x >= len(arr[0]) or y >= len(arr):
      return False
    item = arr[y][x]
    
    if start == (2, 4):
      print(f"aa {current} {item} {nextt}")
    if nextt != None and item != nextt:
      return False
    elif item == "M":
      nextt = "S"
    elif item == "S":
      nextt = "M"
    else:
      return False

  print(f"{start} {item} {nextt}")
  return True


def p2():
  directions = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]

  arr = []
  with open("input.txt", "r") as file:
    for line in file:
      curr = []
      for item in line.strip():
        curr.append(item)
      arr.append(curr)

  starts = []
  for y, line in enumerate(arr):
    for x, item in enumerate(line):
      if item == "A":
        starts.append((x, y))

  count = 0
  for start in starts:
    if all(check_directions_2(direction, start, arr) for direction in directions):
      count += 1

  print(count)

if __name__ == "__main__":
  p2()