class Solution:
    def isPalindrome(self, s: str) -> bool:
        isEven = len(s) % 2 == 0
        mid = len(s) // 2 # gets the lowest mid point
        if isEven:
            mid -= 1
        stack = []
        for i in range(len(s)):
            if i < mid:
                stack.append(s[i])
            elif i == mid and isEven:
                i += 1 # skip the mid part when even, either way it will be in the same position
            else:
                return stack.pop() == s[i]
        return False

print(Solution().isPalindrome(s="anagram"))
print(Solution().isPalindrome(s="rar"))
