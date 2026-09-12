from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for i in strs:
            i_count = Counter(i)
            key = tuple(sorted(i_count.items()))
            if key in hash_table.keys():
                hash_table[key].append(i)
            else:
                hash_table[key] = [i]
        return list(hash_table.values())
