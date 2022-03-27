#Q1 solution:
def g(n):
    sum = 0
    for i in range(1,n+1):
        sum += i/(i+1)
    return sum

for n in range(1,21):
    print(g(n))

#Q2 solution:
def fact(n):
    product = 1
    for i in range(1,n+1):
        product = product*i
    return product

for n in range(1,9):
    print(fact(n))

#Q3 solution:
from math import *
def double_angle_sin(t):
    return(sin(2*t*pi/180))

for i in range(0,100,10):
    print(f"for θ = {i} then sin(2θ) = {double_angle_sin(i)}")

#Q4 solution:
str0 = input("Enter a text: ")
str1 = ""

odd = str0[::2]
even = str0[1::2]

if len(str0)%2 == 0:
    for i in range((len(str0)//2)):
        str1 += even[i] + odd[i]
else:
    for i in range((len(str0)//2)):
        str1 += even[i] + odd[i]
    str1 += odd[len(str0)//2]

print(f"The result is: {str1}")

#Q5 solution:
str0 = input("Enter the string: ")
str1 = ""

f=0
g=0

for i in range(len(str0)):
    if str0[i]==')':
        f=0
        g=1
        continue
    if str0[i]=='(' or f==1:
        f=1
    elif g==0:
        str1+=str0[i]
    g=0
print(str1)

#Q6 solution:
n = int(input("Enter an integer: "))
number = [0]*n

for i in range(n):
    number[i] = int(input(f"Enter value {i+1}: "))
    
odd = 0
even = 0

for i in range(n):
    if number[i]%2 == 0:
        even += 1
    else:
        odd += 1
        
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")

#Q7 solution:
n = int(input("Enter an integer: "))

def summation(n):
    num=3
    c=3
    s=0
    for i in range(1,n+1):
        s+=num
        num=10*num+c
    return(s)

print(f"The sum is: {summation(n)}")

#Q8 solution:
def fact(n):
    product = 1
    for i in range(1,n+1):
        product = product*i
    return product

def strongcheck(n):
    str0 = str(n)
    a = 0
    for i in range(len(str0)):
        num = int(str0[i])
        prod = fact(num)
        a += prod
    if a == n:
        return(True)
    else:
        return(False)
    
for i in range(1,100001):
    if strongcheck(i)==True:
        print(i)
    else:
        continue