# Differentiate between append () and extend () methods?

'''
Python append() method adds an element to a list,
and the extend() method concatenates the first list with another list.
'''

a=[55,"tops",22,True,"python"]
b=[66,"raji",5050,"ahemdabad"]

a.append(b)
print(a)

print("*"*50)

a=[55,"tops",22,True,"python"]
b=[66,"raji",5050,"ahemdabad"]

a.extend(b)
print(a)

