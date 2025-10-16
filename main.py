import random
import sys
inv = ["fists"]
location = "wPark"
money = 100
health = 100
jc = 15

def store(money, health, inv):
  items = ["bandages","g26"]
  price = ["100", "500"]
  i=0
  print("-----STORE-----")
  for item in items:
    print(f"{item.upper()} - ${price[i]}")
    i+=1
  choice = input("Buy item or LEAVE\n")
  if choice.lower() == "bandages":
    if money >= 100:
      money -= 100
      health += 50
      if health > 100:
        health = 100
      print("Purchased bandages")
    else: 
      print("broke")
  if choice.lower() == "g26":
    if money >= 500:
      money -= 500
      inv.append("g26")
      print("bought G26")
    else:
      print("broke")
  print(f"health: {health}\nmoney: ${money}")
  return money, health, inv

def lick(money, health, inv):
  guns = ["g26"]
  robOpt = random.randint(1, 4)
  if robOpt <= 3:
      print("Grandma walking with her purse out")
      choice = input("SNATCH\nGUNPOINT\nASSAULT\n")
      if choice.lower() == "snatch":
        chance = random.randint(1, 4)
        if chance == 1:
          print("She's strong and hits you with her purse")
          health -= random.randint(5, 15)
        else:
          print("You snatch her shit clean")
          money += random.uniform(30, 80)
      elif choice.lower() == "gunpoint":
        chance = random.randint(1,5)
        if chance == 1:
          print("She refuses")
          choice = input("KILL\nLEAVE\n")
          if choice.lower() == "kill":
            print("Grandma's dead")
            money += random.uniform(30, 100)
          if choice.lower() == "leave":
            print("You left grandma alone")
        else:
          print("Grandma hands everything over")
          money += random.uniform(30, 100)
      elif choice.lower() == "assault":
        print("You give grandma the move that made lebron famous")
        chance = random.randint(1,3)
        if chance == 1:
          print("Someone witnesses the commotion and calls the police")
          chance = random.randint(1,3)
          if chance == 1:
            print("G-ma ratted, felony assault, battery, and attempted robbery. Facing 20+ years")
            inv = ["fists"]
            money = 0
            health = 100
          else:
            print("Snatched G-ma's shit and got away without police")
            money += random.uniform(30, 100)
        else:
          print("Mind as well be in antartica because she's out cold")
          money += random.uniform(30, 100)
  elif robOpt == 4:
    print("Theres a store that looks robbable")
    choice = input("WALK away\nGUNPOINT\n")
    if choice.lower() == "gunpoint":
      i = 1
      for item in inv:
        print(f"{i}. {item.upper()}")
        i+=1
      choice = input("Choose item to rob the store with\n")
      for gun in guns:
        if gun.lower() == choice.lower():
          vGun = True
        else:
          vGun = False
        if vGun == True:
          break
      if vGun == True:
        survival = random.randint(1, 8)
        if survival <= 6:
          print("You rob the store at gunpoint")
          money += random.uniform(500, 2000)
        if survival == 7:
          print("One of those off-duty cops superslam your ass and detain you")
          sentence = random.randint(1, 4)
          if sentence == 1:
            print("Judge sentences you to life")
            sys.exit(0)
          else:
            print("Released after 10 years")
            inv = ["fists"]
            money = 0
            health = 100
        elif survival == 8:
          print("Cashier pulls out gun")
          choice = input("FIGHT back\nRUN\n")
          if choice.lower() == "fight":
            survival = random.randint(1, 2)
            if survival == 1:
              print("Cashier puts one between your eyes")
              sys.exit(0)
            elif survival == 2:
              print("You killed the cashier")
              money += random.uniform(500, 2000)
      else:
        print("Store clerk laughs at you")
        choice = input("KILL\nWALK away\n")
        if choice.lower() == "kill":
          i=1
          for item in inv:
            print(f"{i}. {item.upper()}")
          choice = input("Choose item\n")
          if choice.lower() == "fists":
            survival = random.randint(1,3)
            if survival == 1:
              print("You get your shit rocked")
              health -= random.randint(15,40)
            else:
              print("You brutalize him")
        elif choice.lower() == "walk":
          print("You walked away")
    elif choice.lower() == "walk":
      print("You leave")
  print(f"money: ${round(money, 2)}\nhealth: {health}")
  return money, health, inv
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
        elif choice.lower() == "g26":
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
  print(f"health: {health}\nmoney: ${round(money, 2)}")
  return money, health
  
def choices(money, health, location, inv):
  if location == "wPark":
    choice = input("SOUTH to Ashview Heights\nEAST to Vine City\nROB\n")
    if choice.lower() == "south":
      location = "ashview"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
    elif choice.lower() == "east":
      location = "vine"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
    elif choice.lower() == "rob":
      money, health, inv = lick(money, health, inv)
  elif location == "ashview":
    choice = input("NORTH to Washigton Park\nWEST to Mozley Park\nROB\n")
    if choice.lower() == "north":
      location = "wPark"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
    elif choice.lower() == "west":
      location = "mPark"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
    elif choice.lower() == "rob":
      money, health, inv = lick(money, health, inv)
  elif location == "vine":
    choice = input("WEST to Washigton Park\nROB\nSTORE\n")
    if choice.lower() == "west":
      location = "wPark"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
    elif choice.lower() == "rob":
      money, health, inv = lick(money, health, inv)
    elif choice.lower() == "store":
      money, health, inv = store(money, health, inv)
  elif location == "mPark":
    choice = input("EAST to Ashview Heights\nROB\n")
    if choice.lower() == "east":
      location = "ashview"
      if random.randint(1,100) <= jc:
        money, health = jumped(money, health)
    elif choice.lower() == "rob":
      money, health, inv = lick(money, health, inv)
  return money, health, location, inv
print("You are in Washigton Park")
print(f"health: {health}")
print(f"money: {round(money, 2)}")
while True:
  money, health, location, inv = choices(money, health, location, inv)
