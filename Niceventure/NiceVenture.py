from ursina import *
from cow import Cow
from item import Item
from craft import Craft
from tree import Tree
from block import Block
from flowerpot import FlowerPot
from tuffgolem import TuffGolem
from player import Player
from inventory import *

app = Ursina()


import random
import string
#Variaben definieren
mobs_list = ["Zombie", "Kuh", "Schaf", "Schwein"]
mobs_list_forest = ["Wolf", "Fuchs", "Rabe"]
fish_list = ["Barsch", "Lachs", "Forelle", "Tunfisch"]
backpack = ["Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
surrounding = [random.choice(mobs_list), random.choice(mobs_list), random.choice(mobs_list)]
surrounding_forest = [random.choice(mobs_list_forest),random.choice(mobs_list_forest),random.choice(mobs_list_forest)]
biome_list = ["plains", "forest", "ocean"]
current_location = "plains"
current_location_number = 0
e_held = False
inventory_open = False

cow_texture = load_texture('assets/cow.png')
tree_texture = load_texture('assets/tree.png')
grass_texture = load_texture('assets/grass.png')
sword_texture = load_texture('assets/Holzschwert.png')

def update():
    global e_held
    global inventory_open
    global inv_text
    global inv_texture_1
    global inv_texture_2
    global inv_texture_3
    global inv_texture_4
    global inv_texture_5

    if held_keys['escape']: quit()

    if held_keys['e']:
        if not e_held:
            e_held = True
            if not inventory_open:
                inventory_open = True
                inv_text = Text(scale = 1.30, text = "    " + str(inventory[5]) + "\n\n    " + str(inventory[6]) + "\n\n    " + str(inventory[7]) + "\n\n    " + str(inventory[8]) + "\n\n    " + str(inventory[9])) 
                inv_texture_1 = Item(texture = load_texture('assets/' + inventory[0] + '.png'),position = (0, 0))
                inv_texture_2 = Item(texture = load_texture('assets/' + inventory[1] + '.png'),position = (0,-0.55))
                inv_texture_3 = Item(texture = load_texture('assets/' + inventory[2] + '.png'),position = (0,-1.1))
                inv_texture_4 = Item(texture = load_texture('assets/' + inventory[3] + '.png'),position = (0,-1.65))
                inv_texture_5 = Item(texture = load_texture('assets/' + inventory[4] + '.png'),position = (0,-2.2))
            else:
                destroy(inv_text)
                destroy(inv_texture_1)
                destroy(inv_texture_2)
                destroy(inv_texture_3)
                destroy(inv_texture_4)
                destroy(inv_texture_5)
                inventory_open = False
    else:
        e_held = False





#Move
def Move(place:string,slot:int,slot2:int):
    slot -= 1
    slot2 -= 1
    if(place == "B"):
        if(backpack[slot2] == "Nichts"):
            backpack[slot2] = inventory[slot]
            backpack[slot2 + 10] = inventory[slot + 5]
            inventory[slot] = "Nichts"
            inventory[slot + 5] = 0
        elif(backpack[slot2] == inventory[slot]):
            backpack[slot2 + 10] = inventory[slot + 5] + backpack[slot2 + 10]
            inventory[slot] = "Nichts"
            inventory[slot + 5] = 0
    elif(place == "I"):
        if(inventory[slot2] == "Nichts"):
            inventory[slot2] = backpack[slot]
            inventory[slot2 + 5] = backpack[slot + 10]
            backpack[slot] = "Nichts"
            backpack[slot + 10] = 0
        elif(inventory[slot2] == backpack[slot]):
            inventory[slot2 + 5] = backpack[slot + 10]
            backpack[slot] = "Nichts"
            backpack[slot + 10] = 0
    else: 
        print("Unbekannter Speicherplatz. Benutze Inventory (I) oder Backpack (B)")

#Walk
def Walk():
    global current_location_number
    global current_location
    current_location_number += 1
    current_location = biome_list[current_location_number]
    print("Du befindest dich jetzt in einem %s Biom!" %current_location)

#Walk Backwards
def walk_backwards():
    global current_location_number
    global current_location
    current_location_number -= 1
    current_location = biome_list[current_location_number]
    print("Du befindest dich jetzt in einem %s Biom!" %current_location)




for x in range(-10,10):
    block = Block(position = (x,-2.2,2), texture = grass_texture)

cow = Cow(position = (-1,-1))

tree = Tree(position = (2,-1))

craftSword = Craft(position = (6,-3),req = ["Holz"],reqCount = [2],result = "Holzschwert",resultCount = 1)

flower = FlowerPot(position = (-3,-1),texture = load_texture('assets/FlowerPot/FlowerPot1.png'))

golem = TuffGolem(position = (-6,-1))

player= Player(position = (0,-1,-1),texture = load_texture('assets/FlowerPot/FlowerPot2.png'))

app.run()