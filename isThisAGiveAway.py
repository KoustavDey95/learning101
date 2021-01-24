def main():
    r=[]
    t = int(input())
    
    for i in range(t):  
        numbers = myInput()
        r.append(numbers[2])
    display(r)  
def myInput():
    string_input = input()
    input_list = string_input.split()
    input_list = [int(a) for a in input_list]
    return input_list
def display(r):
    for element in r:
        print (element)    
main()   

