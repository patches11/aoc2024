
from codetiming import Timer

def p1():
  arrays = []
  with open("input.txt", "r") as file:
      for line in file:
        items = line.strip().split()
        arrays.append(items)

  diffs = []
  for arr in arrays:
    diff = []
    for i in range(len(arr) - 1):
      diff.append(int(arr[i]) - int(arr[i + 1]))
    diffs.append(diff)

  count = 0
  for diff in diffs:
    p = diff[0]
    if p > 0:
      if all([e > 0 and e <= 3 for e in diff]):
        count += 1
    else:
      if all([e < 0 and e >= -3 for e in diff]):
        count += 1

  print(count)


def internal(arr):
  diff = []
  for i in range(len(arr) - 1):
    diff.append(int(arr[i]) - int(arr[i + 1]))

  p = diff[0]
  if p > 0:
    if all([e > 0 and e <= 3 for e in diff]):
      return True
  else:
    if all([e < 0 and e >= -3 for e in diff]):
      return True

  return False


def p2():
  timer = Timer()
  timer.start()
  arrays = []
  with open("input.txt", "r") as file:
      for line in file:
        items = line.strip().split()
        arrays.append(items)

  count = 0
  for arr in arrays:
    #int_arr = [arr] + [arr[:index] + arr[index+1:] for index in range(len(arr))]
    int_arr = (arr[:index] + arr[index+1:] for index in range(len(arr)+1, 0, -1))
    if any([internal(arr_2) for arr_2 in int_arr]):
      count += 1

  timer.stop()
  print(count)

if __name__ == "__main__":
  p2()