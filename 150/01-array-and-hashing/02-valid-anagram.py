class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # Anagrams have to be of the same length

        map1 = {}
        map2 = {}

        # Populate the maps with the frequencies of each character
        for i in range(len(s)):
            if s[i] in map1:
                map1[s[i]] += 1
            else:
                map1[s[i]] = 1
            if t[i] in map2:
                map2[t[i]] += 1
            else:
                map2[t[i]] = 1

        # Check if the frequencies are the same in both maps
        for k in map1:
            if k not in map2 or map1[k] != map2[k]:
                return False

        return True


print(Solution().isAnagram(s="anagram", t="nagaram"))
print(Solution().isAnagram(s="rat", t="car"))
