import sys

# First Attempt

finalList = []
lower = int(input())  # This is the lowest number of the list
upper = int(input())  # This is the highest number of the list

def sortList(lower, upper):
    for i in range(lower, upper):
        if i % 2 == 0 or i % 7 == 0:  # Check if the number is even or divisible by 7
            finalList.append(i)  # Add to list
    return finalList  # Return list

print(sortList(lower, upper))  # Print all number in between in array


# Second Attempt

lower_limit = int(input("enter lower limit: "))  # This is the lowest number of the list
upper_limit = int(input("enter upper limit: "))  # This is the highest number of the list

def sortList2(lower_limit, upper_limit):
    list = [x for x in range(lower_limit, upper_limit) if (x % 2 == 0 or x % 7 == 0)]
    return list

print(sortList(lower_limit,upper_limit))
