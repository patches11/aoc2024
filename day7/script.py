import itertools

def apply_op(a, b, op):
  if op == "+":
    return a + b
  elif op == "*":
    return a * b
  elif op == "||":
    return int(str(a) + str(b))
  else:
    raise Exception()

ops = ["+", "*"]

ops_2 = ["+", "*", "||"]

def get_result(values, ops):
  a, *b = values
  for i, bb in enumerate(b):
    a = apply_op(a, bb, ops[i])
  return a


def p1():
  rav = []
  with open("input.txt", "r") as file:
      for line in file:
        line = line.strip()
        result, other = line.split(":")
        result = int(result)
        values = [int(a) for a in other.strip().split(" ")]
        rav.append((result, values))
  
  valids = []

  for r, v in rav:
    all_ops = itertools.product(ops, repeat=len(v) - 1)
    if any(r == get_result(v, ops) for ops in all_ops):
      valids.append(r)

  print(sum(valids))


def p2():
  rav = []
  with open("input.txt", "r") as file:
      for line in file:
        line = line.strip()
        result, other = line.split(":")
        result = int(result)
        values = [int(a) for a in other.strip().split(" ")]
        rav.append((result, values))
  
  valids = []

  for r, v in rav:
    all_ops = itertools.product(ops_2, repeat=len(v) - 1)
    if any(r == get_result(v, ops) for ops in all_ops):
      valids.append(r)

  print(sum(valids))
  
if __name__ == "__main__":
  p2()