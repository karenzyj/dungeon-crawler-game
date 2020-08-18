from items import *
import random 

class Store:
  def __init__(self):
    # < Behind the Workshop Part 1 >
    self._capacity = 5 # number of items the store has on sale
    self._items = []   # list of items in the store

  def get_num_items(self): # returns the total number of items in the store
    return len(self._items)

  def refresh(self): # randomly stock store with items
    possible_items = Item.__subclasses__() # each subclass of Item is an item that can appear in the store
    self._items = []
    for slot in range(0, self._capacity):
      self._items.append(random.choice(possible_items)())
  def list_items(self): # print store's items and their prices
    if not self._items:
      self.refresh()
    print("--- Store ---")
    print("#   Item                    Price")
    for i, item in enumerate(self._items):
      print(str(i) + "   " + item.get_name() + "       " + str(item.get_price()) + "g")
  def get_item(self, item_ix): # returns an Item based on its index in self._items
    return self._items[item_ix]
  def remove(self, item): # remove item from store
    self._items.remove(item)
