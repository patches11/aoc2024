
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def create_region(point, arr, in_region):
  x, y = point
  v = arr[y][x]
  candidates = [(x + x1, y + y1) for x1, y1 in directions]
  results = []
  for c in candidates:
    x1, y1 = c
    if c not in in_region and x1 >= 0 and x1 < len(arr[0]) and y1 >= 0 and y1 < len(arr) and arr[y1][x1] == v:
      in_region.add(c)
      results.extend([c] + create_region(c, arr, in_region))
  return results

def perimeter(region, arr):
  perimeter = 0
  for point in region:
      x, y = point
      v = arr[y][x]
      candidates = [(x + x1, y + y1) for x1, y1 in directions]
      for c in candidates:
        x1, y1 = c
        if x1 < 0 or x1 >= len(arr[0]) or y1 < 0 or y1 >= len(arr):
          perimeter += 1
        elif arr[y1][x1] != v:
          perimeter += 1

  return perimeter

def sides(region, arr):
  to_check = set()
  for x, y in region:
    for x1, y1 in directions:
      to_check.add((x, y, x1, y1))
  
  sides = 0
  while len(to_check) > 0:
    x, y, x1, y1 = to_check.pop()
    v = arr[y][x]
    x2, y2 = x + x1, y + y1
    if x2 < 0 or x2 >= len(arr[0]) or y2 < 0 or y2 >= len(arr) or arr[y2][x2] != v:
      sides += 1
    
      outer_elem = x, y, x1, y1

      if x1 != 0:
        inner_dirs = [(0, 1), (0, -1)]
      else:
        inner_dirs = [(1, 0), (-1, 0)]
      for d in inner_dirs:
        n = outer_elem
        x3, y3 = d
        while True:
          x, y, _, _ = n
          n = x + x3, y + y3, x1, y1
          if n in to_check:
            to_check.remove(n)
            x, y, _, _ = n
            x2, y2 = x + x1, y + y1
            if not (x2 < 0 or x2 >= len(arr[0]) or y2 < 0 or y2 >= len(arr) or arr[y2][x2] != v):
              break
          else:
            break

  return sides

def p1():
  arr = []
  with open("input.txt", "r") as file:
      for line in file:
        arr.append(list(line.strip()))

  in_region = set()
  regions = []
  for y in range(len(arr)):
    for x in range(len(arr[0])):
      p = (x, y)
      if p not in in_region:
        in_region.add(p)
        region = [p] + create_region(p, arr, in_region)
        regions.append(region)

  pa = [(perimeter(region, arr), len(region)) for region in regions]

  print(sum([p * a for p, a in pa]))


def p2():
  arr = []
  with open("input.txt", "r") as file:
      for line in file:
        arr.append(list(line.strip()))

  in_region = set()
  regions = []
  for y in range(len(arr)):
    for x in range(len(arr[0])):
      p = (x, y)
      if p not in in_region:
        in_region.add(p)
        region = [p] + create_region(p, arr, in_region)
        regions.append(region)

  pa = [(sides(region, arr), len(region)) for region in regions]

  print(sum([p * a for p, a in pa]))
  
if __name__ == "__main__":
  p2()