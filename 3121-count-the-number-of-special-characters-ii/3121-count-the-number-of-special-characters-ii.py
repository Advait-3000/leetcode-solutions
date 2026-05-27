class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        occ={}
        for pos, letter in enumerate(word):
            if letter not in occ:occ[letter]=[pos]
            else:occ[letter].append(pos)
        count=0
        for i in list(set(word.lower())):
            if i in occ and i.upper() in occ and occ[i][-1]<occ[i.upper()][0]:count+=1
        return count