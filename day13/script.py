import math

def solve(machine):
  i, k = machine["Button A"].values()
  j, l = machine["Button B"].values()
  x, y = machine["Prize"].values()

  b = (x - (i * y) / k) / (j - i * l / k)

  a = (x - j * b) / i

  aa = round(a)
  bb = round(b)

  if i * aa + j * bb == x and k * aa + l * bb == y:
    print("good", machine, a, b)
    return aa, bb
  else:
    
    return None


def p1():
  machines = []
  current = {}
  with open("input.txt", "r") as file:
    for line in file:
        split_a = line.strip().split(": ")

        if len(split_a) == 1:
          machines.append(current)
          current = {}
        else:
          a, b = split_a
          c, d = b.split(",")
          if a == "Prize":
            current[a] = {"x": int(c.split("=")[-1]), "y": int(d.split("=")[-1])}
          else:
            current[a] = {"x": int(c.split("+")[-1]), "y": int(d.split("+")[-1])}
  if current is not None:
    machines.append(current)
    
  solves = []
  for m in machines:
    s = solve(m)
    if s is not None:
      solves.append(s)

  valid = [(a,b, math.gcd(int(a), int(b))) for  a, b  in solves if a <= 100 and a >= 0 and b <= 100 and b >= 0 ]

  v2 = [(3 * a) + b for a,b, g in valid]

  print(sum(v2))

  # 22868 too low
  # Too low 18531
  # Too low 13825

def p2():
  machines = []
  current = {}
  with open("input.txt", "r") as file:
    for line in file:
        split_a = line.strip().split(": ")

        if len(split_a) == 1:
          machines.append(current)
          current = {}
        else:
          a, b = split_a
          c, d = b.split(",")
          if a == "Prize": 
            current[a] = {"x": int(c.split("=")[-1]) + 10000000000000, "y": int(d.split("=")[-1]) + 10000000000000}
          else:
            current[a] = {"x": int(c.split("+")[-1]), "y": int(d.split("+")[-1])}
  if current is not None:
    machines.append(current)
    
  solves = []
  for m in machines:
    s = solve(m)
    if s is not None:
      solves.append(s)

  valid = [(a,b, math.gcd(int(a), int(b))) for  a, b  in solves if a >= 0 and b >= 0 ]

  v2 = [(3 * a) + b for a,b, g in valid]

  print(sum(v2))

  # 89023199918265 too high
  
if __name__ == "__main__":
  p2()