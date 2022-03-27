#Q1 solution:
print(
    """===== Calculator =====
1 - Addition
2 - Subtraction
3 - Multiply
4 - Division
Any other number to exit"""
)

c = int(input("Enter your choice: "))

if c < 1 or c > 4:
    print("Exiting...")
else:
    x = float(input("Enter 1st operand: "))
    y = float(input("Enter 2nd operand: "))

    if y == 0:
        dict = {1: x+y, 2: x-y, 3: x*y, 4: "Undefined division"}
    else:
        dict = {1: x+y, 2: x-y, 3: x*y, 4: x/y}

    print(f"Result = {dict[c]}") #Q1

#Q2 solution:
def distance(x1, y1, x2, y2):
    z = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return round(z, 2)

point1 = input("Enter point 1: ")
point2 = input("Enter point 2: ")
x = point1.split(" ")
y = point2.split(" ")

print(f"The distance between them: {distance(eval(x[0]), eval(x[1]), eval(y[0]), eval(y[1]))}") #Q2

#Q3 solution:
def countWLD(x, y, z):
    s = 2*x + 0*y + z 
    print(f"The point of the team is: {s}")

num = input("Enter the number of wins, loose, draw (space separated): ")
x = num.split(" ")

countWLD(eval(x[0]), eval(x[1]), eval(x[2])) #Q3

#Q4 solution:
def DNAtoRNA(seq):
    listseq = list(seq)
    for i in range(0, len(listseq)):
        if listseq[i] == "T":
            listseq[i] = "U"
    print("".join(listseq))

# #Example:
# DNAtoRNA("GATGGAACTTGACTACGTAAATT")

#To take user input
seq = input("Enter the DNA sequence: ")
DNAtoRNA(seq) #Q4

#Q5 solution:
def ATGC(seq):
    if len(seq) > 1000:
        print("The length of the DNA sequence must be at most 1000")
    else:
        a = seq.count("A")
        b = seq.count("G")
        c = seq.count("T")
        d = seq.count("C")
    print("A:" + str(a) + " C:" + str(d) + " G:" + str(b) + " T:" + str(c))

# #Example:
# ATGC("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")

#To take user input
seq = input("Enter the DNA sequence: ")
ATGC(seq) #Q5

#Q6 solution:
sentence = input("Enter the sentence: ")
s = set((sentence.split()))
l = list(s)
l.sort()
print(' '.join(l)) #Q6

#Q7 solution:
def evaluation(lst, dct, x):
    if x in lst and x in dct:
        print(f"Value of {x} in dictionary is {dct[x]}")
    else:
        print(f"{x} not found in either list or dictionary")

#Example:
lst = ['I','think','therefore','I', 'am','said','Rene','Descartes']
dct = {'Rene' : 0, 'Descartes' : 1, 'I' : 2, 'think': 3}
K = input("Enter the key: ")

evaluation(lst, dct, K) #Q7