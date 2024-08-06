#!/usr/bin/python3

def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    if max_num < 2:
        return None  # No prime numbers if max_num < 2

    # Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    # Generate prime numbers up to max_num
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Cumulative count of primes up to each number
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    # Determine the number of rounds each player wins
    maria_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1

    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # Expected output: "Ben"
