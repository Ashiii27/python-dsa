def max_profit(prices: list[int]) -> int:
    """Return the largest profit from one buy followed by one sell."""
    minimum = float("inf")
    best = 0
    for price in prices:
        minimum = min(minimum, price)
        best = max(best, price - minimum)
    return best
