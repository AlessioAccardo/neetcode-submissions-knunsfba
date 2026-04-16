class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        new_s = ""
        
        for c in s:
            if c.isalnum():
                new_s += c
        
        l, r = 0, len(new_s)-1
        
        new_s = new_s.lower()
        
        while l <= r:
            if new_s[l] != new_s[r]:
                return False
            l+=1
            r-=1
        return True