class Solution:
    def isAnagram(self, s: str, t: str):
        dictonary = {}
        dictonary_2 = {}

        for char in s:
            if char in dictonary:
                dictonary[char] += 1
            else:
                dictonary[char] = 1

        for char in t:
            if char in dictonary_2:
                dictonary_2[char] += 1
            else:
                dictonary_2[char] = 1

        if dictonary == dictonary_2:
            return True
        else:
            return False