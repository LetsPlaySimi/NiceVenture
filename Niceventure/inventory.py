import string

inventory = ["Nichts", "Nichts", "Nichts", "Nichts", "Nichts", 0, 0, 0, 0, 0]

#GiveItem

def GiveItem(item, count):
    for i in range(5):
        if(inventory[i] == "Nichts"):
            inventory[i] = item
            inventory[i + 5] = count
            break
        elif(inventory[i] == item):
            inventory[i + 5] = (inventory[i + 5] + count)
            break

            
#RemoveItems

def RemoveItems(item: string, count: int):
    for i in range(5):
        if(inventory[i] == item and inventory[i + 5] == count):
            inventory[i] = "Nichts"
            inventory[i + 5] = 0
            break
        elif(inventory[i] == item and inventory[i + 5] > count):
            inventory[i + 5] = (inventory[i + 5] - count)
            break

#CheckItems

def CheckItems(item:string,count:int):
    for i in range(5):
        if(inventory[i] == item and inventory[i + 5] >= count):
            return(True)
    return(False)