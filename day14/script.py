
width = 101# 11
height = 103#7

def step_robot(robot):
  x, y, dx, dy = robot

  return (x + dx) % width, (y + dy) % height, dx, dy

def p1():
  robots = []
  with open("input.txt", "r") as file:
    for line in file:
      p, v = line.strip().split(" ")
      x, y = [int(a) for a in p.split("=")[-1].split(",")]
      dx, dy = [int(a) for a in v.split("=")[-1].split(",")]
      robots.append((x, y, dx, dy))

  print(robots)

  for _ in range(100):
    for i, r in enumerate(robots):
      robots[i] = step_robot(r)

  print(robots)

  quadrants = [[0, 0], [0, 0]]
  for r in robots:
    xx = None
    yy = None
    if r[0] < width // 2:
      xx = 0
    elif r[0] > width // 2:
      xx = 1
    if r[1] < height // 2:
      yy = 0
    elif r[1] > height // 2:
      yy = 1
    
    if xx is not None and yy is not None:
      quadrants[xx][yy] += 1
  print(quadrants)

  print(quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1])

  # Too low 87604608


def p2():
  with open("example.txt", "r") as file:
    for line in file:
        line.strip()
  
if __name__ == "__main__":
  p1()