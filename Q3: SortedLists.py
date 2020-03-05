import sys

user_input1 = input("Enter List1 with space in between numbers: ")
list1 = user_input1.split(" ")
user_input2 = input("Enter List2 with space in between numbers: ")
list2 = user_input2.split(" ")

def Diff(list1, list2):
    return[x for x in list2 if x not in list1]  # Check values in List2 if in List1, returns difference

wholeSet = sorted(list1+list2)
difSet = Diff(list1, list2)
resultSet = Diff(difSet, wholeSet)

print(resultSet)
