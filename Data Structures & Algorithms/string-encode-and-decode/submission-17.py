class Solution:

    def encode(self, strs: List[str]) -> str:
        # use non ascii character as a delimiter
        # we need to encode the str
        res = []
        size = []
        for i in strs:
            size.append(len(i))
        for sz in size:
            res.append(str(sz))
            res.append(",")
        res.append("#")
        res.extend(strs)
        return ''.join(res)
            
        


    def decode(self, s: str) -> List[str]:
        res,size,i=[],[],0
        while s[i]!="#":
            j=i
            while s[j]!=",":
                j+=1
            size.append(int(s[i:j]))
            i=j+1
        i+=1
        
        for sz in size:
            res.append(s[i:i+sz])
            i=i+sz
        return res
        
        

        