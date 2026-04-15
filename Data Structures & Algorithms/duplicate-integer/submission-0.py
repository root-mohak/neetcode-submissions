class Solution:
    def hasDuplicate(self, nums):
        seen = []

        for i in nums:
            if i in seen:
                return True
            else:
                seen.append(i)

        return False

        