#!/usr/bin/python3
""" Prime game """


def is_prime(num):
    """ Finds prime number """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """ Finds te winner of the game """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        remaining = set(range(1, n + 1))

        turn = 0
        while remaining:
            current_player = maria_wins if turn % 2 == 0 else ben_wins
            available_primes = [p for p in primes if p in remaining]

            if not available_primes:
                break

            chosen_prime = max(available_primes)
            remaining.difference_update(
                {i for i in range(chosen_prime, n + 1, chosen_prime)}
            )
            turn += 1

        if turn % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
