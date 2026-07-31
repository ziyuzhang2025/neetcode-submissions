class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use hashmap:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=False
            else:
                hashmap[i]=True
        if True in hashmap.values():
            return True
        return False
        