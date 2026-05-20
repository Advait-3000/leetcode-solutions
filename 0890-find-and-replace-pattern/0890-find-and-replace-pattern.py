class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def patt(s):
            index={}
            idx=0
            out=[]
            for i in s:
                if i not in index:
                    index[i]=idx
                    out.append(idx)
                    idx+=1
                else:
                    out.append(index[i])
            return out
        pattern=patt(pattern)
        return [word for word in words if patt(word)==pattern]