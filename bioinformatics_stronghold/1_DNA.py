"""
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

s = input(str())

d = {"A":0, "C":0, "G":0, "T":0}

# Iterate over & count each character in s, then update corresponding key value in d
for k in s:
    d[k] = s.count(k)

# Iterate over keys & values in d, and print each value
for a, b in d.items():
    print(b, end=' ')
