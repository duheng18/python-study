stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items:" + str(item_total))


def addToInventory(inv, addedItems):
    # your code goes here
    for item in addedItems:
        if item in inv:
            inv[item]=inv[item]+1
        else:
            inv[item]=1
    print(inv)
    return inv


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
# displayInventory(stuff)
