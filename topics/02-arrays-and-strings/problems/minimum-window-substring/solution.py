from collections import Counter


def min_window(source: str, target: str) -> str:
    """Return the shortest source substring containing target's counts."""
    if not target or not source:
        return ""
    needed = Counter(target)
    missing = len(target)
    left = start = end = 0
    for right, char in enumerate(source, 1):
        if needed[char] > 0:
            missing -= 1
        needed[char] -= 1
        if missing == 0:
            while left < right and needed[source[left]] < 0:
                needed[source[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
            needed[source[left]] += 1
            missing += 1
            left += 1
    return source[start:end]
