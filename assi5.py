'''
Write a Python function to get the largest number, smallest num and sum
of all from a list.
'''
l=[]
num=int(input("how many elements to put in list: "))
total=0

for i in range(0,num):
    number=int(input("enter element: "))
    l.append(number)
    total=total+number
print("maximum number",max(l))
print("maximum number",min(l))
print("sum of all elements in list=",total)
