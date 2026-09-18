def max_subarray(nums: list[int]) -> int:
    """Return the maximum sum of a non-empty contiguous subarray."""
    if not nums:
        raise ValueError("nums must be non-empty")
    ending_here = best = nums[0]
    for value in nums[1:]:
        ending_here = max(value, ending_here + value)
        best = max(best, ending_here)
    return best
