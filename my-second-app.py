import math as m

for x in range (0,361):
    s=  m.sin(m.radians(x))
    c=  m.cos(m.radians(x))
    power=  m.pow(s,2)+m.pow(c,2)
    print (power)
