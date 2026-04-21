class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(str(len(word)))
            parts.append('#')
            parts.append(word)
        return ''.join(parts)


    def decode(self, s: str) -> List[str]:
        result = []
        L = 0
        i = 0
        j = 0

        while i < len(s):        
            if s[i]=="#":
                L=int(s[j:i])
                result.append(s[i+1:i+L+1])
                i = i+L+1
                j = i
            else:
                i+=1

        return result



        

