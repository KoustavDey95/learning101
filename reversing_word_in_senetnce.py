def myReverse(sentence):
    words = sentence.split()
    for i in range(0,len(words)):
        words[i] = words[i][::-1]

    return (" ".join(words))    


#Test 
_input = "today is saturday"
expectedOutput = "yadot si yadrutas"
observedOutput = myReverse(_input)
result = "PASS" if expectedOutput == observedOutput else "FAIL"
print (result)