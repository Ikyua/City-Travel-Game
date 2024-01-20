import random
import os

GAME_OVER = False  #Determines whether our code will end or not

# Easy Section for Cities

easy = {
  'Toronto': {
    "MILES_TO_GO": 491,
    "PLAYER_MONEY": 500
  },
  'Chicago': {
    "MILES_TO_GO": 789,
    "PLAYER_MONEY": 500
  },
  'Birmingham': {
    "MILES_TO_GO": 962,
    "PLAYER_MONEY": 800
  },
  'Nashville': {
    "MILES_TO GO": 886,
    "PLAYER_MONEY": 700
  },
  'St. Louis': {
    "MILES_TO_GO": 953,
    "PLAYER_MONEY": 1000
  },
  'Baltimore': {
    "MILES_TO_GO": 187,
    "PLAYER_MONEY": 200
  },
  'Washington': {
    "MILES_TO_GO": 226,
    "PLAYER_MONEY": 200
  },
  'Boston': {
    "MILES_TO_GO": 215,
    "PLAYERMONEY": 200
  }
}

# Normal section for Cities
normal = {
  'Miami': {
    "MILES_TO_GO": 1285,
    "PLAYER_MONEY": 1000
  },
  'Denver': {
    "MILES_TO_GO": 1778,
    "PLAYER_MONEY": 1500
  },
}

# Hard cities
hard = {
  'Los Angeles': {
    "MILES_TO_GO": 2789,
    "PLAYER_MONEY": 1500
  },
  'Seattle': {
    "MILES_TO_GO": 2852,
    "PLAYER_MONEY": 1500
  },
  'Pheonix': {
    "MILES_TO_GO": 2409,
    "PLAYER_MONEY": 1500
  },
  'Portland': {
    "MILES_TO_GO": 2894,
    "PLAYER_MONEY": 1500
  },
  'El Paso': {
    "MILES_TO_GO": 2182,
    "PLAYER_MONEY": 1500
  },
  'Oakland': {
    "MILES_TO_GO": 2896,
    "PLAYER_MONEY": 1500
  },
}

# Insane cities
insane = {
  'Anchorage': {
    "MILES_TO_GO": 4358,
    "PLAYER_MONEY": 2500
  },
}

#Introduction to the Game 

print("Welcome to the City Travel Game!\n")
print("This is a text-based travel game that was created in homage to the Oregon Trail Game. The game has a lot of randomizers added into the game that make every travel different from the other.")
print("Your goal of the game is to go from NYC to a specified location of your randomized choosing.\n If you want to learn more about that unique phrasing you should try the game! \n")

print("Hint: If any of your stats reach 0. You will immediately lose the game!\n")
#User's choice of difficulty. Determines, their location, starting currency and distance they have to travel.

cities = 0
while cities == 0:

  print("The City Travel Game\n")

  GAME_TYPE = input(
    "Which difficulity would you like to play? \nEasy: 0-1000 miles \nNormal: 1001-2000 miles \nHard: 2001-3000 \nInsane: 3001-4000 or above miles.\n"
  )
  GAME_TYPE = GAME_TYPE.lower()
  if GAME_TYPE == "easy":
    cities = easy
  elif GAME_TYPE == "normal":
    cities = normal
  elif GAME_TYPE == "hard":
    cities = hard
  elif GAME_TYPE == "insane":
    cities = insane
  else:
    print(f"I don't know what {GAME_TYPE} means?\n")

#Starting the Player with their chosen difficulty stats.
CITY = random.choice(list(cities.keys()))
PLAYER_HEALTH = 5
PLAYER_MONEY = cities[CITY]["PLAYER_MONEY"]
MILES_TO_GO = cities[CITY]["MILES_TO_GO"]
START_DISTANCE = cities[CITY]["MILES_TO_GO"]
CURRENT_DAY = 0
PLAYER_CONSUME = 100

#Introduction to the Game

print("\033[0;36;40m")

print("The City Travel Game\n")

print(f"Your objective is to travel from New York City to {CITY} \nWhile maintaing your important stats. \nBased off how well you progress through the game you can earn medals! \nHere are your ways to get started. ")


def rest():
  #The rest function will add health to the user, decrease their currency and add to their day counter.
  global PLAYER_HEALTH
  global CURRENT_DAY
  global PLAYER_MONEY

  HOTEL_COST = random.randint(100, 200)

  #We limit the user at 5 hp. Whenever they rest, we simply just add to their health but decrease their currency
  if PLAYER_HEALTH < 5:
    PLAYER_HEALTH = PLAYER_HEALTH + 1

  PLAYER_MONEY -= HOTEL_COST

  CURRENT_DAY = CURRENT_DAY + 1
  print(f"You've spent {HOTEL_COST} dollars.")


def eat():
  #The eat function will provide food value to their current stats. Will subtract from their current currency and add to their sustinance value.
  global PLAYER_MONEY
  global PLAYER_CONSUME

  #Food Selection
  foodSelection = input("Where do you want to eat? \n Diner:($100, +10 Sustinance) \n Restaurant:($350, +50 Sustinance) \n Buffet:($225, +30 Sustinance) \n")

  foodSelection = foodSelection.lower()

  #Dinner Selection

  if foodSelection == "diner":
    print(
      "You go to a local diner and order Belguian Waffles. You spent $100 on your meal."
    )
    PLAYER_MONEY -=100
    PLAYER_CONSUME +=20
  #Buffet Selection

  elif foodSelection == "buffet":
    print("You go to an all you can eat buffet and spent $225")
    PLAYER_MONEY -= 225
    PLAYER_CONSUME += 40

  #Restaurant Selection

  elif foodSelection == "restaurant":
    print("You eat a nice beef wellington with a side of mashed potatos at a local restaurant. You spent $350 on your meal")

    PLAYER_MONEY -= 350
    PLAYER_CONSUME +=60

  else:
    print(f"I don't understand what {foodSelection} means")


def stats():
  #The stats function will simply just return your curret stats
  print("\nCURRENT STATS: \n")
  print(f"Health: {PLAYER_HEALTH}")
  print(f"Money: {PLAYER_MONEY}")
  print(f"Day: {CURRENT_DAY}")
  print(f"Miles Left: {MILES_TO_GO}")
  print(f"Sustinace: {PLAYER_CONSUME}")

def drive():
  #The drive function will be the main way for the player to progress through the game. Will subtract from player's distance traveled, value of sustinance, will add to the day counter, will subtract money for "gas", and decrease the player's health by 1.
  global MILES_TO_GO
  global PLAYER_CONSUME
  global CURRENT_DAY
  global PLAYER_MONEY
  global PLAYER_HEALTH

  randomDistance = random.randint(50, 300)
  MILES_TO_GO -=randomDistance

  #Based off the random "distance" that we travel we display a different message for the value that was traveled. 
  
  if randomDistance <= 100:
    print("\033[0;31;40m")
    print(f"Your car broke down, you were only able to drive {randomDistance} miles.")
    PLAYER_CONSUME -= 15

  
  elif randomDistance >= 100 and randomDistance <= 200:
    print("\033[0;32;40m")
    print(f"There was no traffic, you drove, {randomDistance} miles.")
    PLAYER_CONSUME -= 15

  
  elif randomDistance >= 201 and randomDistance <= 300:
    print("\033[0;34;40m")
    print(f"You found a secret shortcut only the FBI knows of you successfuly drove {randomDistance} miles.")
    PLAYER_CONSUME -= 15

  
  CURRENT_DAY += 1
  PLAYER_MONEY -= random.randint(1, 60)
  PLAYER_HEALTH -= 1


def chance_to_win():
  #Profit function. This will randomly select 1 of 4 ways that the user than obtain money. This isn't a choice but mainly ramdonized. Will deduct from the player's sustinance value, deduct from their health, will add to their current currency and add to their day counter.

  global PLAYER_CONSUME
  global PLAYER_MONEY
  global CURRENT_DAY
  global PLAYER_HEALTH
  
  randomJob = random.randint(1, 4)
  
  PLAYER_CONSUME -=15  
  CURRENT_DAY+=1
  
  print('You rolled for a job and have....')

  
  #Option 1: Casino
  if randomJob == 1:
    
    print("entered a local casino, where you test your luck.")
    potentialGain = random.randint(-150, 800)
    PLAYER_MONEY += potentialGain
    print(f"You've gained {potentialGain} dollars")
    PLAYER_HEALTH -= 1

  
  #Option 2: Jepoardy
  elif randomJob == 2:
    print("been selected to be in Jepoardy.")
    potentialGain = random.randint(100, 550)
    PLAYER_MONEY += potentialGain
    print(f"You've gained {potentialGain} dollars")
    PLAYER_HEALTH -= 1

  
  #Option 3: Begging
  elif randomJob == 3:
    print("decided to beg for some money from some good samaratins.")
    potentialGain = random.randint(5, 150)
    PLAYER_MONEY += potentialGain
    print(f"You've gained {potentialGain} dollars")
    PLAYER_HEALTH -=1


  #Option 4: Picking scraps
  elif randomJob == 4:
    print("Found money on the sidewalk instead.")
    potentialGain = random.randint(0, 125)
    PLAYER_MONEY += potentialGain
    print(f"You've gained {potentialGain} dollars")
    PLAYER_HEALTH -=1


#Start of the City Travel Game

while GAME_OVER == False:
  #Check to see if the player had died first before reaching their destination. 
  
  if PLAYER_HEALTH == 0:
    print("You fell asleep while driving and drove into a lagoon causing your death.")
    break

  elif PLAYER_CONSUME <= 0:
    print("You starved to death.")
    break
    
  elif PLAYER_MONEY <= 0:
    print("You couldn't pay for anything, not even a bus fare.")
    break

    
  # Declare the victory of the User!
  
  elif MILES_TO_GO <= 0:
    print(f"You've made it to {CITY}")
    print("\033[0;33;40m")
    print("""
                                   _________
                             .---'::'        `---.
                            (::::::'              )
                            |`-----._______.-----'|
                            |              :::::::|
                          .-|               ::::::|-.
                           \|               :::::/|/
                            |               ::::::|
                            | You have made it to:|
                            | Your destination::::|
                            |               ::::::|
                            |              .::::::|
                            |              :::::::|
                             \            :::::::/
                              `.        .:::::::'
                                `-._  .::::::-'
                                    |     |
                                    |  :::|
                                    |   ::|
                                   /     ::\                                        
                              __.-'      :::`-.__
                             (_           ::::::_)
                              '-----------------'
  """)
    break
#Callings
  choice = input("\n Drive \n Rest \n Profit \n Stats \n Eat \n Quit \n")
  choice = choice.lower()
  os.system('clear')
  
  if choice == "drive":
    print("The City Travel Game\n")
    drive()
    stats()
  elif choice == "eat":
    print("The City Travel Game\n")
    eat()
    stats()

  elif choice == "rest":
    print("The City Travel Game\n")
    print("\033[0;36;40m")
    print("You've decided to rest in a nearby hotel")
    rest()
    stats()
  elif choice == "profit":
    print("The City Travel Game\n")
    chance_to_win()
    stats()
  elif choice == "stats":
    print("The City Travel Game\n")
    print('\033[0;33;40m')
    stats()
  elif choice == "quit":
    break
  else:
    print(f"I'm sorry I don't know what {choice} means")
  print("")
print('\n --------------------------------------------------------------- \n')
print("GAME OVER")
if MILES_TO_GO <= 0:

  print(f"You reached your destination in {CURRENT_DAY} days and had {PLAYER_MONEY} dollars, while driving towards {CITY}")

if PLAYER_HEALTH <= 5 and PLAYER_HEALTH >= 4:
  print("You kept yourself alive and earned a gold in health, impressive.")
elif PLAYER_HEALTH <= 3 and PLAYER_HEALTH >= 2:
  print(
    "You got to your destination but got the flu when you got there thus earning you a silver for health."
  )
else:
  print("You all most died and recieved no medal for health.")
if PLAYER_CONSUME <= 100 and PLAYER_CONSUME >= 80:
  print(
    "You got there well fed and nurished, and recieved a gold in sustanence.")
elif PLAYER_CONSUME <= 79 and PLAYER_CONSUME >= 59:
  print("You got there peckish and was awarded a silver in sustanence.")
elif PLAYER_CONSUME <= 58 and PLAYER_CONSUME >= 38:
  print(
    "You got there with your stomach growling and for that was awarded a bronze medal in sustanence."
  )
else:
  print(
    "You passed out and your grandma had to drag you out of the car and recieved no medal for sustanence."
  )
print("\n ----------------------------------------------------- \n")


#Travel Time Achievements(Easy)


if GAME_TYPE == "easy":
  print("For your Travel Achievements we have:\n")
  if CURRENT_DAY <= 4:
    print("You have achieved GOLD in travel time, good job.")
  elif CURRENT_DAY > 8 and CURRENT_DAY <= 16:
    print(
      "You have achieved SILVER in travel time, you can be quicker then that.")
  elif CURRENT_DAY > 16 and CURRENT_DAY <= 24:
    print(
      "You have achieved BRONZE in travel time, where's your time management skills?."
    )
  else:
    print("You have to do better if you want an award.")

  #Money Achievements(easy)
  
  print("For your Money Achievements we have:\n")
  
  if PLAYER_MONEY >= 1000:
    print(
      "You have achieved PLATINUM in money, I didn't even know that was possible."
    )
  elif PLAYER_MONEY <= 500 and PLAYER_MONEY >= 400:
    print("You have achieved GOLD in money, can't do better then gold, right?")
  elif PLAYER_MONEY <= 399 and PLAYER_MONEY >= 301:
    print("You have a achieved SILVER in money, always room for imporvement.")
  elif PLAYER_MONEY <= 300 and PLAYER_MONEY >= 199:
    print("You have achieved BRONZE in money, how about another try, hmmm?")
  else:
    print("Did you even try to manage your money?")

  #Health

  print("For your Health Achievements we have:\n")
  
  if PLAYER_HEALTH <= 5 and PLAYER_HEALTH >= 4:
    print("You kept yourself alive and earned a GOLD in health, impressive.")
  elif PLAYER_HEALTH <= 3 and PLAYER_HEALTH >= 2:
    print("You got to your destination but got the flu when you got there thus earning you a SILVER for health.")
  else:
    print("You all most died and recieved no medal for health.")

  #Consume
  print("For your Sustinance Achievements we have:\n")
  if PLAYER_CONSUME <= 100 and PLAYER_CONSUME >= 80:
    print(
      "You got there well fed and nurished, and recieved a GOLD in sustanence."
    )
  elif PLAYER_CONSUME <= 79 and PLAYER_CONSUME >= 59:
    print("You got there peckish and was awarded a SILVER in sustanence.")
  elif PLAYER_CONSUME <= 58 and PLAYER_CONSUME >= 38:
    print("You got there with your stomach growling and for that was awarded a BRONZE medal in sustanence.")
  else:
    print("You passed out and your grandma had to drag you out of the car and recieved no medal for sustanence.")
  print("\n ----------------------------------------------------- \n")

#Normal Achievements
#Travel Time(Normal)

if GAME_TYPE == "normal":
  print("For your Travel Achievements we have:\n")
  if CURRENT_DAY <= 12:
    print("You have achieved GOLD in travel time, good job.")
  elif CURRENT_DAY > 16 and CURRENT_DAY <= 26:
    print(
      "You have achieved SILVER in travel time, you can be quicker then that.")
  elif CURRENT_DAY > 28 and CURRENT_DAY <= 32:
    print("You have achieved bronze in travel time, where's your time management skills?.")
  else:
    print("You have to do better if you want an award.")

    #Money Achievements
  print("For your Money Achievements we have:\n")
  if PLAYER_MONEY >= 1800:
    print("You have achieved PLATINUM in money, I didn't even know that was possible.")
  elif PLAYER_MONEY <= 1000 and PLAYER_MONEY >= 800:
    print("You have achieved GOLD in money, can't do better then gold, right?")
  elif PLAYER_MONEY <= 799 and PLAYER_MONEY >= 701:
    print("You have a achieved SILVER in money, always room for imporvement.")
  elif PLAYER_MONEY <= 700 and PLAYER_MONEY >= 600:
    print("You have achieved BRONZE in money, how about another try, hmmm?")
  else:
    print("Did you even try to manage your money?")

  #Health
  print("For your Health Achievements we have:\n")

  if PLAYER_HEALTH <= 5 and PLAYER_HEALTH >= 4:
    print("You kept yourself alive and earned a GOLD in health, impressive.")
  elif PLAYER_HEALTH <= 3 and PLAYER_HEALTH >= 2:
    print("You got to your destination but got the flu when you got there thus earning you a SILVER for health.")
  else:
    print("You almost died and recieved no medal for health.")

  #Consume
  print("For your Sustinance Achievements we have:\n")

  if PLAYER_CONSUME <= 100 and PLAYER_CONSUME >= 80:
    print("You got there well fed and nurished, and recieved a GOLD in sustanence.")
  elif PLAYER_CONSUME <= 79 and PLAYER_CONSUME >= 59:
    print("You got there peckish and was awarded a SILVER in sustanence.")
  elif PLAYER_CONSUME <= 58 and PLAYER_CONSUME >= 38:
    print("You got there with your stomach growling and for that was awarded a BRONZE medal in sustanence.")
  else:
    print("You passed out and your grandma had to drag you out of the car and recieved no medal for sustanence.")
  print("\n ----------------------------------------------------- \n")
#Hard Achievements

if GAME_TYPE == "hard":
  print("For your Travel Achievements we have:\n")

  if CURRENT_DAY <= 14:
    print("You have achieved GOLD in travel time, good job.")
  elif CURRENT_DAY > 18 and CURRENT_DAY <= 28:
    print(
      "You have achieved SILVER in travel time, you can be quicker then that.")
  elif CURRENT_DAY > 30 and CURRENT_DAY <= 34:
    print("You have achieved BRONZE in travel time, where's your time management skills?.")
  else:
    print("You have to do better if you want an award.")

  #Money Achievements
  print("For your Money Achievements we have:\n")
  if PLAYER_MONEY >= 2500:
    print("You have achieved PLATINUM in money, I didn't even know that was possible.")
  elif PLAYER_MONEY <= 1000 and PLAYER_MONEY >= 800:
    print("You have achieved GOLD in money, can't do better then gold, right?")
  elif PLAYER_MONEY <= 799 and PLAYER_MONEY >= 701:
    print("You have a achieved SILVER in money, always room for imporvement.")
  elif PLAYER_MONEY <= 700 and PLAYER_MONEY >= 600:
    print("You have achieved BRONZE in money, how about another try, hmmm?")
  else:
    print("Did you even try to manage your money?")
