import math as m

base = ['A', 'C', 'G', 'U']
codon64 = []
for i in base:
    str0 = ""
    str0 += i
    for j in base:
        str1 = str0 + j
        for k in base:
            str2 = str1 + k
            codon64.append(str2)
# print(codon64)

#Q1 solution:
seq = input("Enter the RNA sequence: ")
seq_list = list(seq)
if len(seq_list)%3 == 0:
    codons = ["".join(seq_list[3*i:3*(i+1)]) for i in range(int(len(seq_list)/3))]
    print(f"Codons are {codons}")

    def freq(x):
        counter = 0
        for i in codons:
            if i == x:
                counter += 1
        return counter/len(codons)

    for x in codon64:
        print(f"freq_{x}: {freq(x)}")
else:
    print("Enter correct RNA sequence.")

#Q2 solution:
amino = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",     
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "Stop",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "Stop",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "Stop",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
} #The dictionary given in page 76 as instructed in the question is not the complete dictionary. So I copied it from a GitHiub repository: https://gist.github.com/stepjue/b2e957215f4e5121fa14. One can easily construct it by Brute force or String-List manipulations.

mRNA = input("Input mRNA sequence: ")
mRNA_list = list(mRNA)
codons = ["".join(mRNA_list[3*i:3*(i+1)]) for i in range(int(len(mRNA_list)/3))]

aminocode = []
for i in range(len(codons)-1): # did -1 for deleting the stop codon from the getting the value.
    aminocode.append(amino.get(codons[i]))

print(aminocode)

#Q3 solution:

r = float(input("Enter the radius: "))

v = (4 * m.pi * r**3)/3
    
print("%f\t %9.1f" %(r, v))
print("%f\t %9.2f" %(r, v))
print("%f\t %9.3f" %(r, v))
print("%f\t %9.4f" %(r, v))

#Q4 solution:
try:
    n = float(input("Enter a number: "))
    sq = m.sqrt(n)
except ValueError:
    print("Not applicable for negative numbers.")
else:
    print(f"Square root of {n} =", format(sq, ".3f"))