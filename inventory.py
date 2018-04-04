# inventory.py
bigBag = {'rope': 1, 'torch': 6, 'dagger': 1, 'arrow': 12}
smallBag = {'silver coin': 50, 'gold coin': 42, 'bronze coin': 60}
bigBagLatch = 1
smallBagLatch = 1
def displayInventory(inventory):
    if bagChoice == 'Big Bag':
        bagName = 'Big Bag'
    if bagChoice == 'Small Bag':
        bagName = 'Small Bag'
    print('Inventory of ' + str(bagName) + ': ')
    item_total = 0
    for k, v in inventory.items():
        if v >= 2:
            print(str(v) + ' ' + str(k) + '(s)')
        else:
            print(str(v)+ ' ' + str(k))
        item_total = item_total + v
    print('Total number of items in ' + str(bagName) + ': ' + str(item_total))
print('There are two bags, a Small Bag and a Big Bag.\nWhich bag would you like to look in to?')
bagChoice = input()
if bagChoice == 'Big Bag':
    bigBagLatch = 0
    displayInventory(bigBag)
    print('The small bag is unopened.\n\nWould you like to open the bag? ')
if bagChoice == 'Small Bag':
    smallBagLatch = 0
    displayInventory(smallBag)
    print('The big bag is unopened.\n\nWould you like to open the bag?')
response = input()
if response == 'Yes' or 'yes' or 'sure':
    if bigBagLatch == 0:
        bagChoice = 'Small Bag'
        displayInventory(smallBag)
        print('\nBoth bags are now opened.')
    if smallBagLatch == 0:
        bagChoice = 'Big Bag'
        displayInventory(bigBag)
        print('\nBoth bags are now opened.')
else:
    print('You leave the other bag unopened.')
    
