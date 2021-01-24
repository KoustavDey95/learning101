def main():
    n=50
    #Insert 1 - 50
    arr=[]
    for i in range(n):
        arr.append(i+1)
    # print (arr) 

    arr.remove(1)
    #Skip 1
    #Start from 2  
    for i in range(0,len(arr)):
        if(i <= len(arr)-1):
            a = arr[i]
            #Inner Loop 
            for j in range(i+1,len(arr)):
                # print(str(arr) + str(j) + " " + str(len(arr)))
                if(j <= len(arr)-1 and arr[j] % a == 0):
                    arr.remove(arr[j])  
                    j=j-1

    print(arr)
main()