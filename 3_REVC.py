"""
Given:  A DNA string s of length at most 1000 bp.
Return: The reverse complement of s.
"""

s = input(str())

print(s.translate(str.maketrans("ATGC", "TACG"))[::-1])



