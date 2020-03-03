import sys

list1 = [1,2,3,4,5,8,4,8,3,6,2]
list2 = [1,3,3,5,5,7,3,7,1,4,8,8,10,9,12]

def Diff(list1, list2):
    return[x for x in list2 if x not in list1]

wholeSet = sorted(list1+list2)
difSet = Diff(list1, list2)
resultSet = Diff(difSet, wholeSet)

print(resultSet)
