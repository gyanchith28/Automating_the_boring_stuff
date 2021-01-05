#Couldn't figure out how to add the delay without module.
import random, time

def Mathquiz():
        x = random.randint(0,9)
        y = random.randint(0,9)
        print(f"{x} x {y}")
        
        chances = 0
        answer = 100
        while(answer != x*y):
            answer= int(input('Your answer is : '))
            try:
                if answer == x*y:
                    print('Correct!!!')
                    break
                else:
                    chances += 1
                    if chances == 3:
                        print('Wrong answer. Moving on.')
                        break
                    print("Try again")
            except ValueError:
                print("Enter an integer.")

for i in range(10):
    time.sleep(1)
    Mathquiz()
