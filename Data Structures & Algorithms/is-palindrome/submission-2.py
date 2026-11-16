class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c
        clean = clean.lower()
        i = 0
        j = len(clean) - 1
        while i < j:
            if clean[i] == clean[j]:
                i += 1
                j -= 1
            else:
                return False
        return True