class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
        n = len(new)-1
        l, r = 0, n
        while l < r:
            if new[l] != new[r]:
                return False
            l += 1
            r -= 1
        return True