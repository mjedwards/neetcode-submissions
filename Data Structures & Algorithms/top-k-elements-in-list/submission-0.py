class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fMap = {}
        for idx, value in enumerate(nums):
            if value not in fMap:
                fMap[value] = 1
            else:
                fMap[value] += 1

        buckets = [[] for _ in range(len(nums)+1)]

        for n in fMap:
            freq = fMap[n]
            buckets[freq].append(n)

        res = []
        for freq in range(len(nums), 0, -1):
            for n in buckets[freq]:
                res.append(n)
                if len(res) == k:
                    return res
        # sorted_dict_desc = dict(sorted(fMap.items(), key=lambda item: item[1], reverse=True))
        # arr = [i for i in sorted_dict_desc]
    
        # res = []
        # for i in range(0, k):
        #     res.append(arr[i])
        
        # return res
