class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sMap = {}
        # for i in strs:
        #     s = ''.join(sorted(i))
            
        #     if s not in sMap:
        #         sMap[s] = [i]
        #     else:
        #         sMap[s].append(i)
        
        # res = []
        # for chars in sMap:
        #     res.append(sMap[chars])

        # return res
        groups = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                counts[index] += 1
            groups[tuple(counts)].append(s)

        return list(groups.values())
