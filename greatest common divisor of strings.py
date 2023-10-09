"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length = min(len(str1), len(str2))
        for i in range(length, 0, -1):
            sub = str1[:i]
            if len(str1)%len(sub) == 0 and len(str2)%len(sub) == 0:
                if sub*(len(str1) // len(sub)) == str1 and sub*(len(str2) // len(sub)) == str2:
                    return sub
        return ""
        
"""
Best solution:
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]
"""