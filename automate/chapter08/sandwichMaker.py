import pyinputplus as pyip
currTotal = 0.00

#Getting bread type
print('What type of bread would you prefer?')
breadMenu = {'wheat': 20.00, 'white' :10.00, 'sourdough' : 5.00}
breadType = pyip.inputMenu(list(breadMenu.keys()))
currTotal += breadMenu[breadType]
print(f'Your current total is Rs.{currTotal}')

#Getting protein type
print('\n',"Protein type are as follows.")
proteinMenu = {'chicken': 30.00, 'turkey' :20.00, 'ham' : 15.00, 'tofu': 25.00}
proteinType = pyip.inputMenu(list(proteinMenu.keys()))
currTotal += proteinMenu[proteinType]
print(f'Your current total is Rs.{currTotal}','\n')

#Asking for cheese
cheese = pyip.inputYesNo(prompt='Need cheese?')
if cheese =='yes':
    cheeseMenu = {'cheddar': 10.00, 'swiss' :15.00, 'mozarella' : 20.00}
    cheeseType = pyip.inputMenu(list(cheeseMenu.keys()))
    currTotal += cheeseMenu[cheeseType]
    print(f'Your current total is Rs.{currTotal}','\n')

addons = pyip.inputYesNo(prompt = 'Need add-ons?')
if addons == 'yes':
    addonsMenu = {'mayo':2, 'mustard':3, 'lettuce':1.5, 'tomato':2.5}
    addonsType = pyip.inputMenu(list(addonsMenu.keys()))
    currTotal += addonsMenu[addonsType]
    print(f'Your current total is Rs.{currTotal}','\n')

numSand = pyip.inputInt(prompt='How many sandwiches would you like to order?', min = 1)
print('\n',f'Your total amount is Rs.{currTotal * numSand}.')
