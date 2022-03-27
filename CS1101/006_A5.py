#Q1 solution:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = min(a, b)
d = max(a, b)

def f(p):
    for i in range(2, p):
        if p%i == 0:
            return False
    return True

prime_list = []
for i in range(c, d+1):
    if f(i) == True:
        prime_list.append(i)

print(prime_list)

#Q2 solution:
import math as m
actual_val = m.exp(m.pi)

def f(x, n):
    term = 1
    mysum = 0
    for i in range(1, n+1):
        mysum += term
        term *= x/i
    return mysum

n = 1
while (actual_val - f(m.pi, n)) >= 10**(-4):
    n += 1

print(f"The number of terms is: {n}")
print(f"The computed value is: {f(m.pi, n)}")
print(f"The actual value is: {actual_val}")
print(f"The absolute difference between the two is: {(actual_val - f(m.pi, n))}")

#Q3 solution:
import math as m
sin_val = m.sin((m.pi) / 2) # = 1
print(sin_val)

def mysin(x, n):
    term = x # term n. 1 = x/1!
    mysum = 0
    for i in range(1, n+1):
        mysum += term
        term *= (-(x**2)) / ((2*i+1) * (2*i))
    return mysum

n = 1
while abs(sin_val - mysin((m.pi)/2, n)) >= 10**(-4):
    n += 1

print(f"The number of terms is: {n}")
print(f"The computed value is: {mysin((m.pi)/2, n)}")
print(f"The actual value is: {sin_val}")
print(f"The absolute difference between the two is: {(sin_val - mysin((m.pi)/2, n))}")

#Q4 solution:
x = "A"
y = " "
for i in range(1, 11):
    print((10-i)*y + 2*i*x + (10-i)*y, end = "\n")

#Q5 solution:
def triangle(x, y, z):
    if x+y>z and y+z>x and z+x>y:
        return True
    return False

x = int(input("Enter the first side length: "))
y = int(input("Enter the second side length: "))
z = int(input("Enter the third side length: "))
if triangle(x, y, z) == True:
    print("A triangle can be formed with given side lengths.")
else:
    print("No triangle can be formed with the given side lengths.")

#Q6 solution:
import math as m
atan_val = m.atan(1) # = pi/4

def myatan(x, n):
    term = x
    mysum = 0
    for i in range(1, n+1):
        mysum += term
        term *= (-x**2) * (2*i - 1)/ (2*i + 1)
    return mysum

n = 1
while 4 * abs(atan_val - myatan(1, n)) >= 10**(-3):
    n += 1

print(f"The number of terms is: {n}")
print(f"The computed value is: {4 * myatan(1, n)}")
print(f"The actual value is: {4 * atan_val}")
print(f"The absolute difference between the two is: {4 * abs(atan_val - myatan(1, n))}")

#Q7 solution:
def f(x):
    return x ** 0.9

n = 0
x = 10
while x >= 2:
    x = f(x)
    n += 1

print(n)