class Solution:
    def _sieve(self, high):
        is_prime = [True] * (high + 1)
        is_prime[0] = is_prime[1] = False # 0 and 1 is not prime
        for num in range(2, int(high**0.5) + 1): # start from 2
            if is_prime[num]:
                for mult in range(num * num, high + 1, num): # eliminate all multiples of num
                    is_prime[mult] = False
        return is_prime

    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_primes = self._sieve(right)
        primes = [num for num in range(left, len(is_primes)) if is_primes[num]]

        result = (-1, -1)
        min_diff = right
        if len(primes) < 2:
            return result

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = (primes[i - 1], primes[i])
        return result
