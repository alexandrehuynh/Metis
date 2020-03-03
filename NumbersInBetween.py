import sys

finalList = []
upper = 1
lower = 22

def sortList(upper, lower):
    for i in range(upper, lower):
        if i % 2 == 0 or i % 7 == 0:  # Check if the number is even or divisible by 7
            finalList.append(i)  # Add to list
    return finalList  # Return list

print(sortList(upper, lower))  # Print all number in between in array

