class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rules = {
            "(":")",
            "[":"]",
            "{":"}"
        }


        for c in s:
            if c in rules:
                stack.append(rules[c])
            elif stack:
                closing = stack.pop()
                if c != closing:
                    return False
            else:
                return False
        return not stack
            
        
            
            
            

            

            