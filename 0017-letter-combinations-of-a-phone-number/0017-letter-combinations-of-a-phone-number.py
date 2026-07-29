class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pos={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        n=len(digits)
        res=[]
        if n==4:
            for i in pos[digits[0]]:
                for j in pos[digits[1]]:
                    for k in pos[digits[2]]:
                        for l in pos[digits[3]]:
                            res.append(i+j+k+l)
            return res
        elif n==3:
            for i in pos[digits[0]]:
                for j in pos[digits[1]]:
                    for k in pos[digits[2]]:
                        res.append(i+j+k)
            return res
        elif n==2:
            for i in pos[digits[0]]:
                for j in pos[digits[1]]:
                    res.append(i+j)
            return res
        else:return pos[digits]