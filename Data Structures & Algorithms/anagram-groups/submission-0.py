class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sMap = {}
        for i in strs:
            s = ''.join(sorted(i))
            
            if s not in sMap:
                sMap[s] = [i]
            else:
                sMap[s].append(i)
        
        res = []
        for chars in sMap:
            res.append(sMap[chars])
            
        return res
