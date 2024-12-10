
def p1():
    with open("input.txt", "r") as file:
        data = file.read().strip()

    idx = 0
    block = True
    arr = []
    for char in data:
      if block:
        arr.extend([idx] * int(char))
        idx += 1
      else:
        arr.extend([None] * int(char))
      block = not block

    done = False
    while not done:
      gap = arr.index(None)
      last_elem = len(arr) - next(i for i,v in enumerate(reversed(arr)) if v is not None) - 1
      if gap >= last_elem:
        done = True
      else:
        arr[gap] = arr[last_elem]
        arr[last_elem] = None

    checksums = [i * v for i, v in enumerate(arr) if v is not None]

    print(sum(checksums))

def p2():
  with open("input.txt", "r") as file:
        data = file.read().strip()

  idx = 0
  block = True
  arr = []
  for char in data:
    if block:
      arr.extend([idx] * int(char))
      idx += 1
    else:
      arr.extend([None] * int(char))
    block = not block


  current_elem = next(v for i,v in enumerate(reversed(arr)) if v is not None)
  while current_elem >= 0:
    elem_start = arr.index(current_elem)
    elem_end = len(arr) - 1 - list(reversed(arr)).index(current_elem)
    elem_len = elem_end - elem_start + 1

    for i in range(0, elem_start):
      r = range(i, i+elem_len)
      if all(arr[x] is None for x in r):
        for x in r:
          arr[x] = current_elem
        for x in range(elem_start, elem_end + 1):
          arr[x] = None
        break

    current_elem -= 1

  checksums = [i * v for i, v in enumerate(arr) if v is not None]

  print(sum(checksums))

  
if __name__ == "__main__":
  p2()