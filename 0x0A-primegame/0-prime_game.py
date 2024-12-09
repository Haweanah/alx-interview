#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # Initialize scores and array of possible prime numbers
    ben = 0
    maria = 0
    # Create a list 'a' of length sorted(nums)[-1] + 1 with all elements
    # initialized to 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # The first two elements of the list, a[0] and a[1], are set to 0
    # because 0 and 1 are not prime numbers
    a[0], a[1] = 0, 0
    # Use Sieve of Eratosthenes algorithm to generate array of prime numbers
    for i in range(2, len(a)):
        rm_multiples(a, i)

