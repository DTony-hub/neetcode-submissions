class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
        result = []
        sorted_keys = sorted(hash_table, key=lambda x: hash_table[x], reverse=True) 
        # sort hash_table theo key
        for i in range(k):
            result.append(sorted_keys[i])
        return result