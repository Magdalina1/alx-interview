#!/usr/bin/python3
""" Module for solving prime game question """

def isWinner(x, nums):
    """function that checks for the winner"""
    if not nums or x < 1:
        return None
    
    max_num = max(nums)
    my_filter = [True for _ in range(max(max_num + 1, 2))]
    
    # Implementing Sieve of Eratosthenes
    for i in range(2, int(max_num ** 0.5) + 1):
        if my_filter[i]:
            for j in range(i * i, max_num + 1, i):
                my_filter[j] = False
    
    my_filter[0] = my_filter[1] = False  # 0 and 1 are not primes
    count_primes = 0
    
    # Counting cumulative primes up to each index
    for i in range(len(my_filter)):
        if my_filter[i]:
            count_primes += 1
        my_filter[i] = count_primes
    
    player1_wins = 0
    
    for n in nums:
        if my_filter[n] % 2 == 1:
            player1_wins += 1
    
    if player1_wins * 2 == len(nums):
        return None
    elif player1_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
