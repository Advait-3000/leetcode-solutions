class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def is_prime(n):
            if n <= 1:return False
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:return False
            return True
        r=int(str(n)[::-1])
        return sum(i for i in range(min(n,r),max(n,r)+1) if is_prime(i))