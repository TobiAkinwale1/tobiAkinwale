import random
import time
import math
from typing import List, Tuple
from itertools import combinations


def calculate_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """
    Calculate Euclidean distance between two 2D points.

    Parameters:
    p1 (Tuple[int, int]): First point as a tuple of x, y coordinates.
    p2 (Tuple[int, int]): Second point as a tuple of x, y coordinates.

    Returns:
    float: Euclidean distance between p1 and p2.
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def validate_input(P: List[Tuple[int, int]], m: int):
    """
    Validate input parameters.

    Parameters:
    P (List[Tuple[int, int]]): List of points as tuples of x, y coordinates.
    m (int): Number of closest pairs to find.

    Raises:
    ValueError: If m is less than 1 or more than the number of unique pairs in P.
    """
    if m < 1 or m > len(P) * (len(P) - 1) // 2:
        raise ValueError("m must be between 1 and n(n-1)/2")


def closest_pairs(P: List[Tuple[int, int]], m: int) -> List[Tuple[Tuple[int, int], Tuple[int, int], float]]:
    """
    Find m closest pairs of points in P.

    Parameters:
    P (List[Tuple[int, int]]): List of points as tuples of x, y coordinates.
    m (int): Number of closest pairs to find.

    Returns:
    List[Tuple[Tuple[int, int], Tuple[int, int], float]]: List of m closest pairs and their distances.
    """
    validate_input(P, m)

    pairs = list(combinations(P, 2))

    pairs_with_dist = [(pair[0], pair[1], calculate_distance(pair[0], pair[1])) for pair in pairs]

    # Sort the list of tuples by the distance
    pairs_with_dist.sort(key=lambda pair: pair[2])

    # Return the first m tuples from the sorted list
    return pairs_with_dist[:m]


def test_performance(P: List[Tuple[int, int]], m: int):
    start_time = time.time()
    closest_pairs(P, m)
    end_time = time.time()
    print(f"Execution time for input size {len(P)}: {end_time - start_time} seconds")


# Example usage
P = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]
m = 3
try:
    result = closest_pairs(P, m)
    for pair in result:
        print(f"Points: {pair[0]}, {pair[1]}, Distance: {pair[2]}")
except ValueError as e:
    print(e)

