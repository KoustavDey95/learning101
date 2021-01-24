# Import math Library
import math

# Return the sine value of 30 degrees
print(math.sin(math.radians(30)))

# Return the sine value of 90 degrees
print(math.sin(math.radians(90)))
for x in range (0,361):
    if  (((math.sin(math.radians(x)))*(math.cos(math.radians(x)))) == 1):
        print(x)

s = 'kd'
s.index('a')
