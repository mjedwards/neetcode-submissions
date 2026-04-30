class Solution:
    def isValid(self, s: str) -> bool:
        sizeOfS = len(s)
        if sizeOfS % 2 != 0: return False

        d = {
            "[": "]",
            "{": "}",
            "(": ")",
        }
    
        order = []

        for i in s:
            if i in d:                
                order.append(d[i])
            else:
                if len(order) == 0: return False

                if order[-1] != i:
                    return False
                else:
                    order.pop()
        return len(order) == 0