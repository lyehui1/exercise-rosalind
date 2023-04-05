"""
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

###Solution 1

s = input(str())

d = {"A":0, "C":0, "G":0, "T":0}

for k in s:
    d[k] = s.count(k)

for a, b in d.items():
    print(b, end=' ')

###Solution 2
# map generates an Iterator.
# The * Operator expands the iterator to function arguments to the print function.

print(*map(input().count, "ACGT"))


###Solution 3

s = input(str())

d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in s:
    d[i] += 1

print(d['A'], d['C'], d['G'], d['T'])