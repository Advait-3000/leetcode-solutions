class Solution:
    def completePrime(self, num: int) -> bool:
        def prime(n):
            if n <= 1:return False
            if n == 2:return True
            if n % 2 == 0:return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:return False
            return True
        s=str(num)
        for i in range(1, len(s) + 1):
            if not prime(int(s[:i])) or not prime(int(s[-i:])):
                return False
        return True