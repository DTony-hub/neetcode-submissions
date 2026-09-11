from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count
        
# Map:
'''
iterate through s and count: O(s)
iterate through t and count: O(t)
'''