import re

def p1():
  with open("input.txt", "r") as file:
    data = file.read()

def p2():
  with open("input.txt", "r") as file:
    for line in file:
      line.strip()
  
if __name__ == "__main__":
  p1()