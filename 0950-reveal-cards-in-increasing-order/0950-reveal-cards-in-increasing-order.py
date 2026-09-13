class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        deck.sort()
        res=[0]*n
        indexs=[i for i in range(n)]
        for card in deck:
            res[indexs.pop(0)]=card
            if indexs:indexs.append(indexs.pop(0))
        return res