moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def in_bounds(pos, arr):
  x, y = pos
  return x >= 0 and x < len(arr[0]) and y >= 0 and y < len(arr)

def check_route(current, arr):
  nexts = [(current[0] + m[0], current[1] + m[1]) for m in moves]
  nexts = [n for n in nexts if in_bounds(n, arr)]
  x0, y0 = current
  cv = arr[y0][x0]
  if cv == 9:
    return set([(x0, y0)])
  results = set()
  for n in nexts:
    x, y = n
    if arr[y][x] == cv + 1:
      results = results.union(check_route(n, arr))
  return results


def check_route_2(current, arr):
  nexts = [(current[0] + m[0], current[1] + m[1]) for m in moves]
  nexts = [n for n in nexts if in_bounds(n, arr)]
  x0, y0 = current
  cv = arr[y0][x0]
  if cv == 9:
    return 1
  results = []
  for n in nexts:
    x, y = n
    if arr[y][x] == cv + 1:
      results.append(check_route_2(n, arr))
  return sum(results)

def p1():
  arr = []
  with open("input.txt", "r") as file:
      for line in file:
        arr.append([int(x) for x in line.strip()])

  starts = []
  for y in range(len(arr)):
    for x in range(len(arr[0])):
      if arr[y][x] == 0:
        starts.append((x, y))
  
  results = []
  for start in starts:
    results.append(check_route(start, arr))

  print(sum([len(r) for r in results]))

def p2():
  arr = []
  with open("input.txt", "r") as file:
      for line in file:
        arr.append([int(x) for x in line.strip()])

  starts = []
  for y in range(len(arr)):
    for x in range(len(arr[0])):
      if arr[y][x] == 0:
        starts.append((x, y))
  
  results = []
  for start in starts:
    results.append(check_route_2(start, arr))

  print(results)
  print(sum(results))

if __name__ == "__main__":
  p2()