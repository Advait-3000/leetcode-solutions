class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n>=49:return True
        elif n>=45:return False
        elif n>=40:return True
        elif n>=34:return False
        elif n>=27:return True
        elif n>=19:return False
        elif n>=10:return True
        else:return False