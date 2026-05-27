class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        reverse=word[::-1]
        n=len(word)
        count=0
        for i in list(set(word.lower())):
            if i in word and i.upper() in word and n-1-reverse.index(i)<word.index(i.upper()):count+=1
        return count