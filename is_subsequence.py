"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false 

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        if len(s) == 0:
            return True
        for t_pointer in range(len(t)):
            if s[s_pointer] == t[t_pointer]:
                if s_pointer == len(s) - 1:
                    return True
                s_pointer += 1

        return False 