class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        # now we have a dict with number and its corresponding count
        # find the top k count
        top_count = []
        for c in sorted(count.values()):
            top_count.append(c)
        #now we have the count of all numbers

        top_k = []
        i= -1
        for j in range(k):
            top_k.append(top_count[i])
            i-=1
        # now we have the top k count 
        res = []
        for key in count:
            if count[key] in top_k:
                res.append(key)
        return res
            