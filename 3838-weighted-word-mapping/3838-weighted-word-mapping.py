class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        letters="zyxwvutsrqponmlkjihgfedcba"
        res=""
        for word in words:
            temp=0
            for letter in word:
                temp+=weights[ord(letter)-ord("a")]
            res+=letters[temp%26]
        return res