#Program to convert lbs to kgs using loops
lbs=[]
kgs=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    elements=int(input("Enter weight of student in lbs: "))
    lbs.append(elements)
    kgs.append(elements*0.453592)
print(lbs)
print(kgs)