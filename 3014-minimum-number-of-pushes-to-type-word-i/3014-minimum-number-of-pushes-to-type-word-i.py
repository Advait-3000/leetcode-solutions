class Solution:
    def minimumPushes(self, word: str) -> int:
        i=1
        count=0
        while len(word)>8:
            count+=8*i
            i+=1
            word=word[8:]
        return count+(len(word)*i)            