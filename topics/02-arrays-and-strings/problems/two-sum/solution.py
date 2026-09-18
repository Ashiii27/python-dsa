def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two distinct values that add to target."""
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []
