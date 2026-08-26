class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        freq={
            "0":0,
            "1":0
        }
        i=0
        small=float('inf')
        strings=[]
        for j in range(len(s)):
            freq[s[j]]+=1
            while freq["1"]>=k:
                if freq["1"]==k and j-i+1<=small:
                    if j-i+1<small:
                        small=j-i+1
                        strings=[s[i:j+1]]
                    else:strings.append(s[i:j+1])
                freq[s[i]]-=1
                i+=1
        return sorted(strings)[0] if strings else ""