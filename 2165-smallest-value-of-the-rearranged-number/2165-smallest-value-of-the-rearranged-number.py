class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:return 0
        if num<0:
            num=sorted(str(num))[::-1]
            num.insert(0,num.pop())
            return int("".join(num))
        num=sorted(str(num))
        if "0" in num:
            num.insert(0,num.pop(num.count("0")))
            # num.remove(num[0])
        return int("".join(num))