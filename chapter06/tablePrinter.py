tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(lst1):
    arrange = []
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            arrange.append(lst1[i][j].rjust(len(max(lst1[i]))))
    
    for i in range(len(lst1[0])):
        x = arrange[i]
        x += " "+ arrange[i + len(lst1[0])] +" " + arrange[i + 2*len(lst1[0])]
        print(x)

printTable(tableData)
