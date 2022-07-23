# What is List? How will you reverse a list?
'''
A list is a data structure in Python that is a mutable,
or changeable, ordered sequence of elements.

Using the reverse() method  can reverse the contents of the list object in-place
i.e., do not need to create a new list instead  just copy the existing
elements to the original list in reverse order. This method directly modifies
the original list.
'''

l=(1,5,'raji',True,'python')
print(list(reversed(l)))
