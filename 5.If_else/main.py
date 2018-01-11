
import math

HEIGHT = 1.75
WEIGHT = 80.5

BMI = math.pow(WEIGHT / HEIGHT, 2)

if BMI > 32:
    print('Too fat')
elif BMI > 28:
    print('Fat')
elif BMI > 25:
    print('Little fat')
elif BMI > 18.5:
    print('Normal')
else:
    print('Too slim')

print('Finish')
