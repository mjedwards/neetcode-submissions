class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        
        for v in cars:
            time = (target-v[0])/v[1]
            if len(stack) == 0:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)

        return len(stack)