"""
Given: A DNA string s having length at most 1000 nt.
Return: The transcribed RNA string of s.
"""

s = input(str())

d = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'U'}

for i in s:
    print(d[i], end = '')
    
