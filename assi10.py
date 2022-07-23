'''
Write a Python function that takes two lists and returns true if they have
at least one common member.
'''
list1=[55,77,3,2,88,59,44]
list2=[40,50,55]

if set(list1)& set(list2):
    print("true")
else:
    print("false")
