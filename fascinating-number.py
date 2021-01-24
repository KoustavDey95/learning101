def isFascinating(number):
    n = number
    if n>99 and n<1000: 
        t=2*n
        u=3*n
        
        
        if t>99 and t<1000 and u>99 and u<1000:
            num=n*(10^6)+t*(10^3)+u
            flag=True
            while num>0:
                digit=num%10
                if digit == 0:
                    flag=False
                    break

                
                copy=num
                ct=0
                if ct>1:
                    flag=False
                    break
                while copy>0:
                    d=copy%10
                    
                    if digit == d:
                        ct=ct+1
                    copy/=10
                    
                 
                num/=10
            if flag == True: 
                print("FASCINATING NUMBER")
            else: 
                print("NOT A FASCINATING NUMBER")
        else:
            print("NOT A FASCINATING NUMBER")
    else:
        print("NOT A FASCINATING NUMBER")

    return flag   

                




#test
# number = 192
# print (number)
# observedOutput = isFascinating(number)
# print (observedOutput)
# result = "PASS" if observedOutput == True else "FAIL"
# print (result)
number = 123
observedOutput = isFascinating(number)
result = "PASS" if observedOutput == False else "FAIL"
print (result)
# number = 219
# observedOutput = isFascinating(number)
# result = "PASS" if observedOutput == True else "FAIL"
# print (result)