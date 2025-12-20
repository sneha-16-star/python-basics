#take input of a string
str1 = input("please enter a sentence")
total=1 #initialize

for i in range(len(str1)):
    #loop will run to calculate the length using string operation
    if(str1[i]==' '):
        #condition 1
        total = total + 1
print("total number of words in this string =",total)      