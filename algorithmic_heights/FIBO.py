"""
Given: A positive integer n ≤ 25.
Return: The value of Fibonacci index Fn.
"""

n = int(input())

old = 1
new = 1

for i in range(n-1):
    tmpVal = new
    new = old
    old = old + tmpVal

print(new)
