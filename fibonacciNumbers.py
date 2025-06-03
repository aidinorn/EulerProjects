#Problem 2

#By considering the terms in the Fibonacci sequence whose values do not exceed four million,find the sum of the even-valued terms.

listOfNums = [1,1] # 2 First Number of Fibonacci Numbers
indexNum=0

while True :
    number= listOfNums[indexNum] + listOfNums[indexNum + 1] #Formula Of Next Number

    if number >= 4000000 :
        break
    listOfNums.append(number) #Update List Of Numbers
    indexNum+=1 #Go TO Next Index

evenListOfNums = [num for num in listOfNums if num %2==0] #Checking Even Numbers In List Of Numbers
print(sum(evenListOfNums))