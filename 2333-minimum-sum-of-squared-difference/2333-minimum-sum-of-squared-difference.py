class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        total_k=k1+k2
        diffs=[abs(a-b) for a,b in zip(nums1,nums2)]
        if sum(diffs)<=total_k:return 0
        freq=Counter(diffs)
        unique_diffs = sorted(freq.keys(),reverse=True)
        i=0
        while i<len(unique_diffs) and total_k>0:
            curr_max=unique_diffs[i]
            next_diff=unique_diffs[i+1] if i+1<len(unique_diffs) else 0
            count=freq[curr_max]
            drop=curr_max-next_diff
            total_needed=count*drop
            if total_k>=total_needed:
                total_k-=total_needed
                freq[next_diff]+=count
                del freq[curr_max]
            else:
                quotient,remainder=divmod(total_k,count)
                new_val=curr_max-quotient
                del freq[curr_max]
                freq[curr_max-quotient]+=count-remainder
                freq[curr_max-quotient-1]+=remainder
                total_k=0
                break
            i+=1
        return sum(diff*diff*count for diff,count in freq.items() if diff>0)