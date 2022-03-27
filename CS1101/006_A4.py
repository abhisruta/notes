#Q1 solution:
l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
s = []
for i in range(len(l)):
    if (type(l[i]) == list):
        for j in range(len(l[i])):
            s.append(l[i][j])
    else:
        s.append(l[i])
print(s)

#Q2 solution:
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
matrix = []
for i in range(1, r+1):
    l = []
    for j in range(1, c+1):
        print(f"Enter element at row number {i} and column number {j}:", end=' ')
        a = int(input())
        while a < -999 or a > 999:
            a = int(input("Enter number within the range [-999, 999]"))
        l.append(a)
    matrix.append(l)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=' ')
    print()

#Q3 solution:
l = [3, 7, 13, 9, 7, 5, 13, 17, 23, 17, 7, 29]
s = set(l)
l1 = list(s)
print(l1)

#Q4 solution:
l = []
s = 1 #setting counter as non-zero integer.
while s != 0:
    s = int(input("Enter a non-zero integer (enter ing 0 will terminate the input process): "))
    if (s != 0):
        l.append(s)
    else:
        break
print(f"The list of entered non-zero integers is {l}") #4.1
if l != []:
    print(f"The average of the non-zero integers entered is {sum(l)/len(l)}")
else:
    print(f"No non-zero integers were entered. So average is 0") #4.2

#Q5 solution:
numbers = []
for i in range(1,101):
    numbers.append(i)
print(numbers) #5.1
squares = []
for i in range(1,101):
    squares.append(i)
    squares.append(i*i) 
print(squares) #5.2

#Q6 solution:
squares = {1:1,2:4,3:9,4:16,5:25}
for i in range(6,10):
    squares[i] = i**2
print(squares)
print(squares.pop(1))

#Q7 solution:
array = [[1, 2, 3, 4],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]
for i in range(0,4):
    array[i].remove(array[i][-1])
print(array)

#Q8 solution:
d = {'a': 100, 'b':200, 'c':300}
s = 0
for i in d:
    s += d[i]
print(s)

#Q9 solution:
t_o_t = (('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'), ('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'))
print(t_o_t[0][3],",",t_o_t[1][4])
print(t_o_t[0][0],",",t_o_t[1])

#Q10 solution:
l = eval(input("Enter the list: "))
d = {}
for i in range(len(l)-2):
    d[l[i]] = l[i+2]
print(d)