# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""print("happy birthday")
c="abc"
d="efg"
print(c+d)

for i in range(5):
    print(i) """
#x=type('23')
#print(x)

#x=type(eval('23'))
#print(x)

#x=12.3892
#y=format(x,".2f")
#print(y)

#a=12345757.464657
#y=format(a,">4.1f")
#print(y)

#B=[12,"hi",'orange',24.6]
#print(B[1:-2])

#C=[12,"hi",'orange',24.6,'Mango','grapes','cat',234,'dog','grapes']
#C[1:3]='rjv'
#C.insert(1,'10')
#print(C)
#C.remove("24.6")
#print(C)
#x1=C.count('grapes')
#print(x1)
#print(C)
#z=[1,8,45,98,34,90,23,37]
#Z=sorted(z,reverse=False)
#z.sort()
#print(list(reversed(z)))
#listB=list((12,13,18))
#print(listB)

#a=()
#print(type(a))

#k=123456789.654321
#print(format(k,"<5.1f"))

#z=[1,8,45,98,34,90,23,37]
#z.sort()
#print(z

"""lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")"""


# concatenate
n1=input("enter the string")
n2=input("enter the second string")
print(n1+n2)

#reverse
n3=input("enter the third string")
print(n3[::-1])

# string operation
print(n1[:-1])
print(n2[0:6])
print(n1.upper())
print(n1.lower())
print(n1.index('n'))
print(n1.startswith("T"))

s={'3','4','5'}
t="-"
print(t.join(s))

# Reverse string function
def r(a):
    st=""
    for i in a:
     st=i+st
    return st
a='twinkle'
print(r(a))

#concatenate function
def c(b,d):
    conca=b+d
    return conca
b= "ME in"
d=" AI"
print(c(b,d))




