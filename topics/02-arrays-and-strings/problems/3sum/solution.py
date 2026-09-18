def three_sum(nums: list[int]) -> list[list[int]]:
    """Return all unique value triplets whose sum is zero."""
    nums = sorted(nums)
    result: list[list[int]] = []
    for first in range(len(nums) - 2):
        if first and nums[first] == nums[first - 1]:
            continue
        if nums[first] > 0:
            break
        left, right = first + 1, len(nums) - 1
        while left < right:
            total = nums[first] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[first], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result
