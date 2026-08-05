class Solution:

    def encode(self, strs: List[str]) -> str:
        # use non ascii character as a delimiter
        # we need to encode the str
        res,size=[],[]
        for s in strs:
            size.append(len(s))
        for sz in size:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)




    def decode(self, s: str) -> List[str]:
        
        size,res,i=[],[],0
        while s[i]!="#":
            j=i
            while s[j]!=",":
                j+=1
            size.append(int(s[i:j]))
            i=j+1
        i+=1
        # the above is to fill in the size list and leave i at the correct position
        for sz in size:
            res.append(s[i:i+sz])
            i+=sz

        return res

        