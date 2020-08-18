class Item:
  def __init__(self, name, price):
    self._name = name
    self._price = price

  def get_name(self):
    return self._name
  def get_price(self):
    return self._price

## Consumable Items ##
# all items must be constructed with a name and a price
# all items must have a use() function which determines the effect they have
class Small_Health(Item):
  def __init__(self):
    super().__init__("Small Health Potion", 25)
  def use(self, character):
    character.heal(round(character.get_max_hp() * 0.6)) # restores 60% of max health

class Large_Health(Item):
  def __init__(self):
    super().__init__("Large Health Potion", 50)
  def use(self, character):
    character.heal(round(character.get_max_hp() * 0.8)) # restores 80% of max health

# < Behind the Workshop Part 3 > (uncomment code block below)
# class Super_Health(Item):
#   def __init__(self):
#     #### YOUR CODE HERE ####
#   def use(self, character):
#     #### YOUR CODE HERE ####

class Small_Mana(Item):
  def __init__(self):
    super().__init__("Small Mana Potion", 25)
  def use(self, character):
    # can only be used by a mage
    if character.get_rpg_class() == "Mage": 
        character.restore_mana(round(character.get_max_mana() * 0.6)) # restores 60% of max mana
    else:
      print("Potion has no effect because " + character.get_name() + " is not a mage.")
      
class Large_Mana(Item):
  def __init__(self):
    super().__init__("Large Mana Potion", 50)
  def use(self, character):
    # can only be used by a mage
    if character.get_rpg_class() == "Mage": 
        character.restore_mana(round(character.get_max_mana() * 0.8)) # restores 80% of max mana
    else:
      print("Potion has no effect because " + character.get_name() + " is not a mage.")
