def f(n):
    s = 0.0
    for i in range(n):
        s+=i
    return s
print(f(5))

def f(n):
    if n==1:
        return 1
    else:
        return 3*f(n-1)

print(f(4))

def f(n):
    s = 0
    for i in range(n):
        y = float(2*i)/n
        if y**2 < y:
            s += 1
    return s
print(f(100))

string = "mind your train"
str_new = string.split()
str_out = ""
for i in range(len(str_new)-1, -1, -1):
    str_out = str_out + " " + str_new[i]

str_out = str_out.lstrip().rstrip()
print(str_out)

m = 25
if (m<40):
    grace = 10
elif (m<50):
    grace = 5
else:
    reward = 5
grace = 0

m += grace

print(m)



def f(x):
    if x%2 == 0:
        return x
    else:
        return x+1
print(f(3), f(4))

# surnames = ["m", "s", "d", "s", "m"]
# out = {"m": [], "s": [], "d": []}
# for i in range(len(surnames)):
#     if surnames[i] in out:
#         out[surnames[i]].append(i)

# print(out)

# t = (1,2,3,4)
# t.append((5,6,7))
# print(len(t))

def f(x):
    return 1 - x**2
r = 0.0
while f(r)>0:
    r += 0.2

print(r)


try:
    f.open("demofile.txt")
    f.write("abcd")
except:
    print("Something")
finally:
    f.close()