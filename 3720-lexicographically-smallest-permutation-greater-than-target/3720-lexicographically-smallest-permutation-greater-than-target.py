class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        if "".join(sorted(s)[::-1])<=target:return ""
        n=len(s)
        m=len(target)
        freq=Counter(s)
        ans=[]
        length=0
        for i in target:
            if freq[i]>0:
                freq[i]-=1
                ans.append(i)
                length+=1
            else:break
        for i in range(length,-1,-1):
            if i<m:
                tar=target[i]
                candidates=sorted([i for i in freq if i>tar and freq[i]>0])
                if candidates:
                    chosen=candidates[0]
                    freq[chosen]-=1
                    return "".join(ans[:i]+[chosen]+[i*freq[i] for i in sorted(freq)])
            if i>0:
                freq[ans[i-1]]+=1