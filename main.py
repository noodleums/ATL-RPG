import random
import sys
inv = ["fists", "g27"]
location = "wPark"
money = 50
health = 100
jc = 100
def jumped(money, health):
  ynAmount = random.randint(2,4)
  print(f"A group of {ynAmount} YNs jump you")
  while True:
    choice = input("RUN\nFIGHT\nCOMPLY\n")
    if choice.lower() == "run":
      survival = random.randint(1,4)
      if survival == 1:
        print("You try to run but they dome your bitchass")
        sys.exit(0)
      elif survival == 4:
        print("You successfuly get away without consequence")
        break
      else:
        print("You try to escape but they pop you and run your pockets")
        health -= random.randint(20,50)
        money *= .70
        break
    elif choice.lower() == "fight":
      i = 1
      for item in inv:
        print(f"{str(i)}. {item.upper()}")
        i += 1
      while True:
        choice = input("Choose item to defend yourself\n")
        if choice.lower() == "fists":
          survival = random.randint(1,5)
          if survival == 1:
            print("You got lit up like the 4th of July")
            sys.exit(0)
          elif 2 <= survival <= 4:
            print("They shot you and took your money")
            health -= random.randint(40, 70)
            money *= .70
            break
          else:
            print("You give them move that made lebron famous and they scatter")
            break
          break
        elif choice.lower() == "g27":
          survival = random.randint(1,6)
          if survival <= 4:
            print("You shoot them but they get you too before they run off")
            health -= random.randint(30,50)
          else:
            print("Get domed fn")
            sys.exit(0)
          break
      break
    elif choice.lower() == "comply":
      print("They run your pockets twin")
      money *= random.randint(6,8)/10
      break
    else:
      print("Invalid answer choice")
  if health <= 0:
    print("You succumb to your injuries")
    sys.exit(0)
  print(f"health: {health}\nmoney: ${money}")
  return money, health
  
def choices(money, health, location):
  if location == "wPark":
    choice = input("SOUTH to Ashview Heights\nEAST to Vine City\n")
    if choice.lower() == "south":
      location = "ashview"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
    elif choice.lower() == "east":
      location = "vine"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
  elif location == "ashview":
    choice = input("NORTH to Washigton Park\nWEST to Mozley Park\n")
    if choice.lower() == "north":
      location = "wPark"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
    elif choice.lower() == "west":
      location = "mPark"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
  elif location == "vine":
    choice = input("WEST to Washigton Park\n")
    if choice.lower() == "west":
      location = "wPark"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
  elif location == "mPark":
    choice = input("EAST to Ashview Heights\n")
    if choice.lower() == "east":
      location = "ashview"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
  return money, health, location
print("You are in Washigton Park")
print(f"health: {health}")
print(f"money: ${money}")
while True:
  money, health, location = choices(money, health, location)
