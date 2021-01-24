def main(): 
    t = int(input())
    r = []
    for i in range(t):
        n = int(input())
        f = myInput()
        r.append(distanceCovered(n,f))
    display(r)

def myInput():
    string_input = input()
    input_list = string_input.split()
    input_list = [int(a) for a in input_list]
    return input_list

def distanceCovered(n,f):
    flag=True
    i,fuel,distance=0,0,0
    while flag==True and i<n:
        
        fuel+=f[i]
        if fuel>0:
            distance+=1
        fuel-=1
        i+=1
        if fuel<0:
            flag=False
    if not(fuel < 0):
        distance+=fuel
    return distance

def display(r):
    for element in r:
        print(element)
main()

