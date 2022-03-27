# This is Assignment 1 of CS1101.

# @author Abhisruta Maity, 21MS006.
# email ID: am21ms006@iiserkol.ac.in

#This file is submitted to CS1101 via WeLearn academic portal.

#Question 1 Solutions
# Given cmd python to start python shell in terminal. #Q1a
x = list(range(10)) #Q1b
y = list(range(3,13)) #Q1c
print(x[::-1]) #Q1d
print(x[1:10:2])
print(x[:9:2]) #Q1e
if x[3] == y[0]:
    print(f"The elements are equal and equal to: {x[3]}")
else: 
    print("The elements are not equal") #Q1f
if 10 in x:
    print("10 is in the list x")
else:
    print("10 is not in the list x") #Q1g
if 7 in y:
    print("7 is in the list y")
else:
    print("7 is not in the list y") #Q1h
print(x + y) #Q1i
z = x[::-1] + y #stored the combined list in z
print(z.index(max(z)))
print(z.index(min(z))) #Q1j

#Question 2 Solutions
x = "The quick brown fox jumps over the lazy dog" #Q2a
if x.find("fox") < 0:
    print("The word fox is not in the sentence.")
else:
    print(f"""The word fox is in the sentence, whose index starts from: {x.find("fox")}""") #Q2b
p = list(x)
p.reverse()
q = ''.join(p)
print(q) #Q2c
r = x.split(" ")
print(r[::3]) #Q2d
print(r[::4]) #Q2e
print(len(x)) #Q2f
print(p[::2]) #Q2g
w = list(x)
y = w[:3:]
z = w[len(w)-3:len(w):]
print(y + z) #Q2h
print(y*10) #Q2i

#Question 3 Solutions
x = 1.2 #Q3a
y = 12 #Q3b
z = 24 #Q3c
print(x/y, y/z, z/x)
print(type(x/y) == float)
print(type(y/z) == float)
print(type(z/x) == float) #Q3d
print(3**7) #Q3e
print(2.0**3 == 8.0) #Q3f
print((y + z) == str(y) + str(z)) #Q3g

#Question 4 Solutions
print("Hello World") #Q4a
# This is a comment. #Q4b
name = "Abhisruta"
age = "18"
roll = "21MS006"
print(name)
print(age)
print(roll)
print(f"Hello! My name is {name}. I am {age} years old. My roll number is {roll}") #Q4c
a = input("Enter your first number: ")
b = input("Enter your second number: ")
print(a + b) #Q4d
c = int(input("Enter your first number: "))
d = int(input("Enter your second number: "))
print(c + d) #Q4e
print("It's good to learn Python") #Q4f
print("""The man asked, "Where to meet you?" I said, "Well, use Google Meet!" """) #Q4g
b = 4.0 # we take a float variable.
print(type(b)) #Q4h
Name = input("What's your name? ")
print(f"My name is {Name}") #Q4i
name = input("What's your name? ") 
age = int(input("What's your age? "))
while True:
    gender = input("What's your gender? Male or Female or Transgender: ")
    if gender == "Male" or gender == "Female" or gender == "Transgender":
        print(f"Good Morning {name}! You are a {gender} of {age} years.")
        break
    print("Gender is wrong. Please retry.") #Q4j

#Acknowledgements: Thanks to the instructors for providing this assignment.