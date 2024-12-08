import itertools
def p1():
  nodes = {}
  with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
          if c != ".":
            arr = nodes.get(c, [])
            arr.append((x, y))
            nodes[c] = arr

  ly = y + 1
  lx = x + 1

  antinodes = set()

  for arr in nodes.values():
    for a in arr:
      for b in arr:
        if a != b:
          diff_y = a[1] - b[1]
          diff_x = a[0] - b[0]
          y = a[1] + diff_y
          x = a[0] + diff_x
          if x >= 0 and x < lx and y >= 0 and y < ly:
            antinodes.add((x, y))

  print(len(antinodes))

def p2():
  nodes = {}
  with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
          if c != ".":
            arr = nodes.get(c, [])
            arr.append((x, y))
            nodes[c] = arr

  ly = y + 1
  lx = x + 1

  antinodes = set()

  for arr in nodes.values():
    for a in arr:
      for b in arr:
        if a != b:
          diff_y = a[1] - b[1]
          diff_x = a[0] - b[0]
          antinodes.add(a)
          aa = a
          oob = False
          while not oob:
            y = aa[1] + diff_y
            x = aa[0] + diff_x
            aa = (x, y)
            if x >= 0 and x < lx and y >= 0 and y < ly:
              antinodes.add((x, y))
            else:
              oob = True

  print(len(antinodes))
  
if __name__ == "__main__":
  p2()