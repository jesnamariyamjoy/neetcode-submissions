from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Convert the list to a tuple so it can be used as a dictionary key
            res[tuple(count)].append(s)
            
        return list(res.values())