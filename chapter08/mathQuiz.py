import pyinputplus as pyip
import random, time

total = 10
correct = 0
for i in range(total):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' %(i, num1, num2)

try:
    pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit= 3)
    
