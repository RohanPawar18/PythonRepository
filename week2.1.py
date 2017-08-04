i=6
i=6+1.0
print(type(i))
s = 'hello\'s hello'
s=10
print(s)
print(type(s))

s="hello"
print(s[:5])  # Sub-string
print(s[-3:-1])

#List
l1 = [True,10,"uhkgxd"]
print(l1)

# ////////// List MUTABLE property///////////
l2 = [[2,[37]],4,["abc"]]
l3=l2
l2[1]=5
print("List 2:  ",l2,"\nList 3:  ",l3)

#////// To make copy of list use full slice//////////
l3 = l2[:]
l2[1]=4
print("List 2:  ",l2,"\nList 3:  ",l3) 

#///////////// Equality
l2 = l3[:]
l2[1] = 10
if(l2 is l3) :
    print("Same list")
else:
    print("Different lists")

#//////////////// List concatenation////////
l4 = l2+l3
print("New list l4= ",l4)
