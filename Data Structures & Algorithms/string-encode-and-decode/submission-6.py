class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        if not strs: return "empty"
        if len(strs) == 1 and strs[0] == "": return encoded_str
        

        for i in range(len(strs)):
            if i == len(strs) - 1:
                encoded_str += strs[i]
            else:
                encoded_str += strs[i] + "€"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "": return [""]
        if s == "empty": return []
        return s.split("€")
            