
def p1():
  l1 = []
  l2 = []
  with open("input1.txt", "r") as file:
      for line in file:
        s = line.strip().split(" ")
        l1.append(int(s[0]))
        l2.append(int(s[-1]))

  distances = []

  l1.sort()
  l2.sort()

  for i, elem1 in enumerate(l1):
    elem2 = l2[i]

    distances.append(abs(elem1 - elem2))

  print(sum(distances))

def p2():
  l1 = {}
  l2 = {}
  with open("input1.txt", "r") as file:
      for line in file:
        s = line.strip().split(" ")
        l1[int(s[0])] = l1.get(int(s[0]), 0) + 1
        l2[int(s[-1])] = l2.get(int(s[-1]), 0) + 1

  print(l1, l2)
  scores = []
  for k, v in l1.items():
    elem2 = l2.get(k, 0)

    scores.append(k * v * elem2)

  print(sum(scores))


if __name__ == "__main__":
  p2()