"""Probability mess around"""

from random import getrandbits


def coin_flip_simulation(num_flips) -> float:
    """Simulations"""
    tails = getrandbits(num_flips).bit_count()
    heads = num_flips - tails
    return heads / num_flips


print(f"Percentage of Heads: {coin_flip_simulation(10000)}")

