from collections import defaultdict


def subarray_sum(nums: list[int], target: int) -> int:
    """Count contiguous subarrays whose sum equals target."""
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    prefix = answer = 0
    for value in nums:
        prefix += value
        answer += prefix_count[prefix - target]
        prefix_count[prefix] += 1
    return answer
