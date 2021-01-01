def arrange(lst1):
    if len(lst1) == 0:
        return ''
    elif len(lst1) == 1:
        return(lst1[0])
    else:
        string1 = str(lst1[0])
        for i in range(1, len(lst1) - 1):
            string1 = string1 + ', ' + str(lst1[i])
        string1 += ' and ' + str(lst1[-1])
        return string1

spam = ['apples', 'bananas', 'tofu', 'cats']
print(arrange(spam))
