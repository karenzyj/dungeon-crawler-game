import random
class Character:
  def __init__(self, name, rpg_class, hp, attack_pow, dodge_chance, speed):
    self._name = name
    self._rpg_class = rpg_class # e.g. knight, mage, rogue
    self._hp = hp # current health points
    self._max_hp = hp # maximum health points
    self._attack_pow = attack_pow # base attack power
    self._dodge_chance = dodge_chance # chance to dodge attack as a decimal (0.6 = 60%)
    self._speed = speed # speed - determines who goes first in battle and whether character can escape battle
    self._ran_away = False # whether or not character ran away from fight
    self._gold = 0 # gold is won in battles and can be used to purchase items
    self._items = [] # character's inventory
  
  def get_name(self):
    return self._name
  def get_rpg_class(self):
    return self._rpg_class
  def get_hp(self):
    return self._hp
  def get_max_hp(self):
    return self._max_hp
  def get_speed(self):
    return self._speed
  def get_ran_away(self):
    return self._ran_away

  def print_stats(self):
    print("\n- " + self._name + " Stats -")
    print("Class: " + self._rpg_class)
    print("HP: " + str(self._hp) + "/" + str(self._max_hp))
    if self._rpg_class == "Mage":
      print("Mana: " + str(self._mana) + "/" + str(self._max_mana))
    print("Attack Power: " + str(self._attack_pow))
    print("Dodge Chance: " + str(self._dodge_chance))
    print("Speed: " + str(self._speed))
  
  # < Behind the Workshop Part 4 >
  #### YOUR CODE HERE ####


  
  ####

  # Combat Functions
  def is_dead(self): # returns True if character's HP is 0 or lower
    return self._hp <= 0
  def attack(self, other): # is called when this character attacks another character (other)
    # damage dealt is a random value within 2 points of the character's base attack power (i.e. if base attack power is 4, then damage can be any integer from 2 to 6)
    damage = self._attack_pow + random.randint(-2,2) 
    if damage <= 0: # damage cannot be less than 1; if it is, set to 1
      damage = 1
    print(self._name + " attacks " + other.get_name() + " for " + str(damage) + " damage!")

    # < Behind the Workshop Part 2 > 
    #### YOUR CODE HERE ####

    other.take_damage(damage) # the other character takes damage
  def take_damage(self, damage): # is called when this character is the victim of an attack
    # determines whether the character dodges the attack
    if random.random() >= self._dodge_chance:
      # character did not dodge; character loses HP equal to damage taken
      self._hp -= damage
      print(self._name + " lost " + str(damage) + " HP!")
    else:
      # character dodged; no damage taken
      print(self._name + " dodged the attack!")
  def heal(self, heal_amount): # is called when character restores HP
    old_hp = self._hp
    self._hp += heal_amount
    if self._hp > self._max_hp: # HP after healing cannot exceed character's maximum HP
      self._hp = self._max_hp
      heal_amount = self._hp - old_hp
    print(self._name + " recovered " + str(heal_amount) + " HP!")
    print(self._name + " now has " + str(self._hp) + "/" + str(self._max_hp) + " HP.")
  def set_ran_away(self, state): # changes the value (boolean) of the _ran_away attribute 
    self._ran_away = state

  # Store Functions
  def buy(self, item, store): # is called when character purchases an item from the store
    # does character have enough gold to afford the item?
    if self._gold >= item.get_price():
      print(self._name + " bought " + item.get_name() + " for " + str(item.get_price()) + " gold.")
      store.remove(item) # remove item from store
      self._items.append(item) # add item to character's inventory
      self._gold -= item.get_price() # subtract gold from character
      print(self._name + " now has " + str(self._gold) + " gold.")
    else:
      print(self._name + " cannot afford this item!")

  # Inventory Functions
  def get_gold(self):
    return self._gold
  def add_gold(self, gold): # adds a specified amount of gold
    self._gold += gold
  def subtract_gold(self, gold): # subtracts a specified amount of gold
    self._gold -= gold
  def list_items(self): # print the contents of the character's inventory
    print("\n--- Inventory ---")
    if self._items:
      for i, item in enumerate(self._items):
        print(i, item.get_name())
    else:
      print("No items in inventory.")
  def add_item(self, item): # add an item to the character's inventory
    self._items.append(item)
  def use_item(self): # use an item from the character's inventory
    self.list_items() # list character's inventory
    item_idx = input("Type the number of the item you want to use, or type 'n' to cancel: ")
    try:
      item_idx = int(item_idx)
      if item_idx in range(0, len(self._items)):
        item = self._items[item_idx] # retrieve Item object corresponding to index
        print(self._name + " used " + item.get_name() + "!")
        item.use(self) # use item
        self._items.remove(item) # remove item from inventory
      else:
        print(self._name + " doesn't have an item with that number.")
        self.use_item() # repeat prompt
    except ValueError: # handles cases where user input is not an integer
      if item_idx == 'n':
        return False # return False if character decided not to use an item
      else:
        print("Invalid input.")
        self.use_item() # repeat prompt 
    return True # return True if an item was used

###############################################
#### RPG Classes (subclasses of Character) ####
###############################################
class Knight(Character):
  def __init__(self, name):
    super().__init__(name, "Knight", 15, 3, 0.2, 4)

class Mage(Character):
  def __init__(self, name):
    super().__init__(name, "Mage", 13, 5, 0.3, 5)
    self._mana = 20 # magical energy
    self._max_mana = 20
    self._mana_attack_cost = 2 # amount of mana needed for each attack
  def get_mana(self):
    return self._mana
  def get_max_mana(self):
    return self._max_mana

  def attack(self, other):
    # can only attack if mage has enough mana
    if self._mana >= self._mana_attack_cost: 
      super().attack(other)
      self._mana -= self._mana_attack_cost
      print(self._name + " used " + str(self._mana_attack_cost) + " mana. " + self._name + " has " + str(self._mana) + " mana left.")
    else:
      print(self._name + " does not have enough mana to attack!")
  def restore_mana(self, restore_amount): # restore character's mana
    old_mana = self._mana
    self._mana += restore_amount
    if self._mana > self._max_mana: # mana cannot exceed mage's max mana
      self._mana = self._max_mana
      restore_amount = self._max_mana - old_mana
    print(self._name + " restored " + str(restore_amount) + " mana!")
    print(self._name + " now has " + str(self._mana) + "/" + str(self._max_mana) + " mana.")

class Rogue(Character):
  def __init__(self, name):
    super().__init__(name, "Rogue", 10, 4, 0.6, 8)

#############################################
#### Enemy Class (subclass of Character) ####
#############################################
class Enemy(Character):
  def __init__(self):
    # enemy's name and stats are randomly chosen
    name_bank = ["Orc", "Goblin", "Troll", "Ghoul", "Harpy", "Wraith", "Werewolf"]
    super().__init__(random.choice(name_bank), "Monster", random.randint(5,10), random.randint(1,4), random.randint(1,6) / 10., random.randint(1,10))