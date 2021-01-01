import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    lst1 = []
    for i in range(100):
        x = random.randint(1,2)
        if x == 1:
            lst1.append('H') # 1 for heads
        else:
            lst1.append('T') #2 for tails

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    for i in range(99):
        if lst1[i] == lst1[i+1]:
            streak += 1
        else:
            if streak % 6 == 0 and streak != 0:
                numberOfStreaks += 1
            streak = 0
print('Chance of streak: %s%%' % (numberOfStreaks / 100))