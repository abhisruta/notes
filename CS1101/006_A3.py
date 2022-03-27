#Q1 solution:
n = int(input("Enter the number upto which you need the sum: "))
square = 0
cube = 0
for i in range(n):
    square += (i+1)**2
    cube += (i+1)**3

formula_square = (n * (n+1) * (2*n + 1)) /6
formula_cube = ((n * (n+1)) / 2) ** 2

print(square)
print(cube)

print(square == formula_square)
print(cube == formula_cube)

#Q2 solution:
numlist = []
n = int(input("Enter the number: "))
for i in range(n):
    numlist.append(2*i + 1)
    numlist.append(0)
print(numlist)

#Q3 solution:
n = int(input("Enter the value of n: "))
sumlist = []
sum = 0
for j in range(1, (n+1)):
    sum = 0
    for i in range(1, j+1):
        sum += (i)**2
    sumlist.append(sum)
print(sumlist)

#Q4 solution:
n = int(input("Enter number of terms: "))
a = 1
b = 0
for i in range(1,n+1):
	b=1+(i/a)
	a=b
print(b)

#Q5 solution:
fibonacci = []
n = int(input("Enter the number of terms: "))
x = 1
y = 1
if n == 1: 
    fibonacci.append(x)
    print(fibonacci)
elif n == 2:
    fibonacci.append(x)
    fibonacci.append(y)
    print(fibonacci)
else:
    fibonacci.append(x)
    fibonacci.append(y)
    for i in range(n-2): #because already two entries are added.
        z = x + y
        x = y
        y = z
        fibonacci.append(z)
    print(fibonacci)

#Q6 solution:
p = int(input("Enter a non-negative integer: "))

while p < 0:
    print(f"invalid input: {p}")
    p = int(input("Enter a non-negative number: "))

s = p ** (1/2)
print(f"The square root of the number that you entered is {s}")

#Q7 solution:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
t = (name, age)
print(t) #7.1

studentlist = []
for i in range(10):
    a = input(f"Enter the name of student {i+1}: ")
    b = int(input(f"Enter the age of the student {i+1}: "))
    c = (a, b)
    studentlist.append(c)

print(studentlist) #7.2 

#Q8 solution:
n = input("Enter the mobile number: ")
numlist = []
for x in range(10):
    if n.find(str(x))==- 1:
        numlist.append(x)

print(f"In your number {n}, {numlist} are not present.")

#Q9 solution:
student_list = ["20MS004", "20MS100", "20MS019", "20MS064", "20MS158", "20MS231", "20MS244","20MS190"]
groupA = []
groupB = []
for i in student_list:
    if int(i[4:]) < 150:
        groupA.append(i)
    else:
        groupB.append(i)

print(f"Group A is {groupA}")
print(f"Group B is {groupB}")

#Q10 solution:
Farenhite = [0,0,0,0,0]
Celcius = [0,0,0,0,0]
for i in range (5):
    x = float(input("Enter Farenhite Temperature: "))
    Farenhite[i] = x
    Celcius[i] = ((x-32)*(5/9))
    
print("The Celcius equivalents are: " + str(Celcius))

#Q11 solution:
marks = []
for i in range(5):
    m = int(input("Course Marks: "))
    marks.append(m)

print(tuple(marks))
for i in marks:
    if i < 50:
        marks[marks.index(i)] += 5
print(tuple(marks))