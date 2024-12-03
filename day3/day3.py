import re

def p1():
  with open("input.txt", "r") as file:
      data = file.read()
        
  matches = re.findall(r'mul\(\d+,\d+\)', data)

  items = []
  for match in matches:
    a = match[4:-1].split(',')
    items.append(int(a[0]) * int(a[1]))

  print(sum(items))

def p2():
  with open("input.txt", "r") as file:
      data = file.read()

  matches = re.findall(r'mul\(\d+,\d+\)|don\'t|do', data)

  enabled = True
  items = []
  for match in matches:
    if match == "do":
      enabled = True
    elif match == "don't":
      enabled = False
    elif enabled == True:
      a = match[4:-1].split(',')
      items.append(int(a[0]) * int(a[1]))

  print(sum(items))

if __name__ == "__main__":
  p2()