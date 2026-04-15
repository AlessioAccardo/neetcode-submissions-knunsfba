class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for word in strs:
            encoded_str += str(len(word)) + "€" + word
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        n = len(s)
        
        # 2.we3.say1.:3.yes10.!@#$%^&*()
        while i < n:
            length = ""
            while s[i] != "€":
                length += s[i]
                i += 1
            w_len = int(length)
            res.append(s[i+1:i+1+w_len])
            i += w_len+1
        return res
            