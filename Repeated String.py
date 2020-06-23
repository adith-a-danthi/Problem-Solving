# HackerRank - Repeated String
# Lilah has a string 's' of lowercase English letters that she repeated infinitely many times.
# Given an integer 'n' find and print the number of letter a's in the first 'n' letters of Lilah's infinite string.
# Constraints:
# 1 <= |s| <= 100
# 1 <= n <= 10^12

# Sample Input:
# aba
# 10

# Sample Output:
# 7

s = input()
n = int(input())

count = s*(n//len(s)) + s[:(n%len(s))]
print(count)