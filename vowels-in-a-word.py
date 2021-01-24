#Function to input a character and check whether vowel or not
def isVowel(i):
    if i=="a" or i=="e"or i=="i"or i=="o"or i=="u" or i=="A" or i=="E"or i=="I"or i=="O"or i=="U":
        return True
    return False

#Taking User Input
word=input("Enter a word")
ct=0

for i in word.lower():
    if isVowel(i):
        ct=ct+1
print ("Count: "+str(ct))        

