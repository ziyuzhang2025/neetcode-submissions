class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,zero_cnt =[],0
        product= 1
        for i in nums:
            if i!=0:
                product*=i
            else:
                zero_cnt +=1
        if zero_cnt >1:
            return [0]*len(nums)
        if zero_cnt==1:
            for i in nums:
                if i!=0:
                    res.append(0)
                else:
                    res.append(product)
        elif zero_cnt ==0:
            for i in nums:
                res.append(int(product/i))
        return res
