class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dictionary to store all the distinct elements 
        # this method makes use of ascii
        res= defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            count = tuple(count)
            res[count].append(s)
        return list(res.values())
