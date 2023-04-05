"""
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

###Solution 1

s = input(str())

d = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'U'}

for i in s:
    print(d[i], end = '')
    


###Solution 2 (with .replace())
dna = "GATGGAACTTGACTACGTAAATT"
rna = dna.replace("T", "U")

print(rna)


###Solution 3 (with .replace())
s = input()
print(s.replace("T", "U"))