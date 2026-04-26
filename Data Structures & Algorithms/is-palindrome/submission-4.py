class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalize = ''.join([i.lower() for i in s if i.isalnum()])
        middle = len(normalize)//2
        l = middle - 1
        r = middle + 1
        if len(normalize) % 2 == 0:
            r = middle

        while l >= 0 and r < len(normalize):
            if normalize[l] != normalize[r]:
                return False
            l-=1
            r+=1
             
        return True
        