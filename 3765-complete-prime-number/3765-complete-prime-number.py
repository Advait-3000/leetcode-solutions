class Solution:
    def completePrime(self, num: int) -> bool:
        def isPrime(n):
            if n <= 1:return False
            if n == 2:return True
            if n % 2 == 0:return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:return False
            return True
        prefix=[num]
        suffix=[num]
        for i in range(1,len(str(num))):
            suffix.append(num%(10**i))
            prefix.append(num//(10**i))
        for i in prefix:
            if not isPrime(i):return False
        for i in suffix:
            if not isPrime(i):return False
        return True