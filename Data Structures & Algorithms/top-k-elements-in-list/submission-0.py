class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hashmap = {}

        for num in nums:
            if num in count_hashmap:
                count_hashmap[num] += 1
            else:
                count_hashmap[num] = 1

        sorted_items = sorted(count_hashmap.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result