from tqdm.auto import trange

def apply_inner(item):
  if item == 0:
    return [1]
  elif len(str(item)) % 2 == 0:
    stringed = str(item)
    l = len(stringed) // 2
    return [int(stringed[:l]), int(stringed[l:])]
  else:
    return [item * 2024]

def apply_rule(data, i):
  new_offset = 0
  if data[i] == 0:
    data[i] = 1
  elif len(str(data[i])) % 2 == 0:
    stringed = str(data[i])
    l = len(stringed) // 2
    data[i] = int(stringed[:l])
    data.insert(i+1, int(stringed[l:]))
    new_offset += 1
  else:
    data[i] = data[i] * 2024
  return data, new_offset

def p1():
    with open("input.txt", "r") as file:
        data = [int(a) for a in file.read().strip().split(" ")]

    for _ in trange(25, miniters=1):
      offset = 0
      for i in trange(len(data), leave=False):
        data, new_offset = apply_rule(data, i+offset)
        offset += new_offset

    print(len(data))
    # 194557

computed = {}

def compute_one(input, left, store=True):
    key = f"{input}-{left}"
    if left == 0:
      return 1
    elif key in computed:
      return computed[key]
    else:
      result_1 = apply_inner(input)
      result = 0
      for r in result_1:
        result += compute_one(r, left-1, store=True)
      if store:
        computed[f"{input}-{left}"] = result
      return result
      
def p2():
  with open("input.txt", "r") as file:
        data = [int(a) for a in file.read().strip().split(" ")]

  r = 75
  result = []
  for i in trange(len(data)):
    result.append(compute_one(data[i], r))

  print(sum(result))
  
if __name__ == "__main__":
  p2()