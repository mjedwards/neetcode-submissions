class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        temp_stack = []

        for i, t in enumerate(temperatures):
            while temp_stack and temperatures[temp_stack[-1]] < t:
                prev = temp_stack.pop()
                res[prev] = i - prev
            temp_stack.append(i)

        return res
            
            


        