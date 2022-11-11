class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_s = s.lower()
        new = "".join(filter(str.isalnum, lowercase_s))
        return new == new[::-1]