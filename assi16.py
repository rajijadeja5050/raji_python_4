# Write a Python program to get unique values from a list.

l=[44,66,23,53,86,98,44,72,66,34,86,36,53,44]
print("original list:",l)

my_list=set(l)
my_new_list=list(my_list)
print("list of unique numbers:",my_new_list)
