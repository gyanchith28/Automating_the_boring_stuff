def collatz(num):
        if num % 2 == 0:
            return num//2
            
        else:
            return 3*num + 1

try:
    n = int(input())
    while n!=1:
        n = collatz(n)
        print(n)
        

except ValueError:
    print('ERROR : Enter an integer')
