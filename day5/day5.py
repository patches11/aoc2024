import re

def check_rule(update, i, item, rules, debug=False):
  for rule in rules:
    if item == rule[0]:
      check = update[i:]
      if debug:
        print(update, i , item, rule[1], check)
      if rule[1] not in check:
        return False
    elif item == rule[1]:
      check = update[:i]
      if debug:
        print(update, i , item, rule[0], check)
      if rule[0] not in check:
        return False
  return True

def rule_applies(item, order, update):
  if item not in order:
    return False
  other = order[order.index(item) - 1]
  if other not in update:
    return False
  return True

def p1():
  orders = []
  updates = []
  with open("input.txt", "r") as file:
    for line in file:
      if "|" in line:
        orders.append(line.strip().split("|"))
      elif "," in line:
        updates.append(line.strip().split(","))

  valids = []
  for update in updates:
    valid = True
    for i, item in enumerate(update):
      applicable_rules = [order for order in orders if rule_applies(item, order, update)]
      if not check_rule(update, i, item, applicable_rules):
        valid = False
    if valid:
      valids.append(int(update[len(update) // 2]))

  print(sum(valids))


def p2():
  orders = []
  updates = []
  with open("input.txt", "r") as file:
    for line in file:
      if "|" in line:
        orders.append(line.strip().split("|"))
      elif "," in line:
        updates.append(line.strip().split(","))

  valids = []
  for v, update in enumerate(updates):
    valid = True
    for i, item in enumerate(update):
      applicable_rules = [order for order in orders if rule_applies(item, order, update)]
      if not check_rule(update, i, item, applicable_rules):
        valid = False
    if valid:
      valids.append(v)

  invalids = [update for v, update in enumerate(updates) if v not in valids]

  corrects = []
  for v, update in enumerate(invalids):
    all_applicable_rules = [rule for rule in orders if rule[0] in update and rule[1] in update ]

    valid = False 
    while valid == False:
      switched = False
      for i, item in enumerate(update):
        gt_rules = [rule[0] for rule in orders if rule[0] in update and rule[1] == item ]
        for ii, other in enumerate(update[i+1:]):
          if other in gt_rules:
            update.insert(i + ii + 2, update.pop(i))
            switched = True
            break
      if not switched:
        valid = True
    corrects.append(update)        

  valids = []
  for correct in corrects:
    valids.append(int(correct[len(correct) // 2]))

  print(sum(valids)) 

  
if __name__ == "__main__":
  p2()