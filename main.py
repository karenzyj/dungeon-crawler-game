from characters import *
from items import *
from store import *
import random


#################
#### Battles ####
#################
def battle(player, enemy): # handles encounters between a player and an enemy
  round_num = 1 # keeps tracks of rounds in the fight
  go_first = player.get_speed() >= enemy.get_speed() # the faster character goes first
  player.set_ran_away(False) 
  # battle continues as long as neither character is dead and player has not run away
  while not player.is_dead() and not enemy.is_dead() and not player.get_ran_away():
    print("== Round " + str(round_num) + " ==")
    print(player.get_name() + " has " + str(player.get_hp()) + " HP.")
    print(enemy.get_name() + " has " + str(enemy.get_hp()) + " HP.")
    if go_first:
      player_turn(player, enemy) # player makes a move
      enemy_turn(player, enemy) # enemy makes a move
    else:
      print(enemy.get_name() + " is faster than " + player.get_name() + "!")
      enemy_turn(player, enemy)
      player_turn(player, enemy)
    print()
    round_num += 1
  
  if enemy.is_dead(): # if player killed enemy, player earns gold 
    print(enemy.get_name() + " died!")
    gold_reward = random.randint(10,100)
    player.add_gold(gold_reward)
    print(player.get_name() + " earned " + str(gold_reward) + " gold.")
    print(player.get_name() + " now has " + str(player.get_gold()) + " gold.\n")
    return True # return True if player was victorious - this immediately exits the function
  if player.is_dead():
    print(player.get_name() + " died!")
  return False # return False if player was killed or if player ran away


def player_turn(player, enemy): # handles player's actions in battle
  if not player.is_dead():
    # prompt player to take an action
    action = ""
    while action not in ['1', '2', '3', '4']:
      action = input("What will " + player.get_name() + " do? Type 1 to attack, 2 to use item, 3 to view stats, or 4 to run away: ")

    if action == '1':
      player.attack(enemy)
    elif action == '2':
      used_item = player.use_item() # used_item stores a boolean (whether or not an item was actually used)
      if not used_item: # if player changed mind about using item, repeat action prompt
        print()
        player_turn(player, enemy)
    elif action == '3':
      player.print_stats()
      print()
      player_turn(player, enemy) # repeat action prompt after printing stats
    else:
      # player's speed must be greater than or equal to enemy's speed to run away
      if player.get_speed() >= enemy.get_speed():
        print("Got away safely!\n")
        player.set_ran_away(True)
      else:
        print("Failed to run away!")
  

def enemy_turn(player, enemy): # handles enemy's actions in battle
  # enemy should only attack if it is not dead and if player has not ran away
  if not enemy.is_dead() and not player.get_ran_away():
    enemy.attack(player)


############################
#### Visiting the Store ####
############################
def visit_store(player, store): # handles player's choices when visiting a store
  print("")
  store.refresh() # refresh all items in the store
  store.list_items() # print the store's items
  print("\n" + player.get_name() + " has " + str(player.get_gold()) + " gold.")
  choice = input("Would you like to buy anything? (y/n): ")
  while choice == 'y':
    print("")
    store.list_items()
    item_idx = input("Type the number of the item you want to buy, or type 'n' to cancel: ")
    try:
      item_idx = int(item_idx)
      if item_idx in range(0, store.get_num_items()): # make sure index is valid
        item = store.get_item(int(item_idx)) # retrieve Item object corresponding to index
        player.buy(item, store) # purchase item
      else:
        print("There is no item with this number.")
    except ValueError: # handles cases where user input is not an integer
      if item_idx == 'n': 
        break # exit loop if player changes mind about buying something
      else:
        print("Invalid input.")
    choice = input("Would you like anything else? (y/n): ")
  print(player.get_name() + " leaves the store.\n")


############################
#### Character Creation ####
############################
def create_character():
  # prompt user for character's name
  name = input("What is your character's name? ")

  # prompt user to choose a RPG class
  rpg_class = ""
  while rpg_class not in ["knight", "rogue", "mage"]:
    rpg_class = input("What is your character's class? Choose from Knight, Mage, or Rogue: ").lower()
  # construct an object called player belonging to the user's chosen class
  if rpg_class == "knight":
    player = Knight(name)
  elif rpg_class == "mage":
    player = Mage(name)
  else:
    player = Rogue(name)

  print("Your character's name is " + player.get_name() + ".")
  print(player.get_name() + " is a " + player.get_rpg_class() + ".")
  player.print_stats() # print the character's stats
  print("\n")

  return player


###################
#### Game Loop ####
###################
def play_game(player):
  continue_game = True 
  num_kills = 0 # keeps score of how many monsters the player has killed
  store = Store() # create a Store object called store
  while continue_game: # keep playing until user decides to exit game
    print("=== Crossroads ===")
    
    # < Behind the Workshop Part 4 >
    #### YOUR CODE HERE ####

    ####

    # prompt user to choose an action
    print("What should " + player.get_name() + " do?")
    choice = ""
    while choice not in ['1', '2', '3', '4', '5']:
      choice = input("Type 1 to fight, 2 to use item, 3 to visit the store, 4 to view stats, or 5 to exit the game: ")
    if choice == '1':
      enemy = Enemy() # create an Enemy object called enemy
      print("\nA wild " + enemy.get_name() + " appears!")
      enemy.print_stats() # print enemy's stats
      print()
      victory = battle(player, enemy) # battle() returns True if player defeated enemy
      if victory:
        num_kills += 1
      if player.is_dead(): # if player dies, game automatically ends
        print("Game over!")
        continue_game = False
    elif choice == '2':
      player.use_item()
      print("\n")
    elif choice == '3':
      visit_store(player, store)
    elif choice == '4':
      player.print_stats()
      print()
    else: # user decided to exit game
      print("\nGoodbye!")
      continue_game = False 
    print("Monsters killed: " + str(num_kills) + "\n\n")


##############
#### Main ####
##############
# Behold the beauty of abstraction... calling this one simple method launches the entire game :)
def main():
  player = create_character()
  play_game(player)

if __name__ == '__main__':
  main()