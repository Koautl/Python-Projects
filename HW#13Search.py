def BinarySearch(numberList,numberGuess):
   left = 0
   right = len(numberList) - 1
   count = 0
   success = False
   while left <= right:
       count = count +1
       mid = left + (right - left) // 2
       if numberList[mid] == numberGuess:
           success = True
           break
       elif numberList[mid] < numberGuess:
           left = mid + 1
       else:
           right = mid - 1
   if(success != False):
        print("Using Binary search the number" + str(numberGuess) + " was found in " + str(count) + "# comparisons.")
   if(success == False):
        print("Using Binary search the number " + str(numberGuess) + " was not found in " + str(count) + "# comparisons.")

def sequentialSearch(numberList,numberGuess):
    count = 0
    for x in numberList:
        count += 1
        if(x == numberGuess):
            print("Using Sequential search the number " + str(numberGuess) + " was found in " + str(count) + "# comparisons.")
            return
    print("Using Sequential Search the number " + str(numberGuess) + " was not found in " + str(count) + "# comparisons.")


import random
def main():
    numberList = [0] * 20
    for x in range(20):
        numberList[x] = random.randint(0,20)
    print(numberList)
    sortedList = sorted(numberList)
    numberGuess = int(input('What number would you like to search for?'))
    print("the number you have chosen to search for is ",numberGuess)
    BinarySearch(sortedList, numberGuess)
    sequentialSearch(sortedList, numberGuess)
if __name__ == "__main__":
    main()