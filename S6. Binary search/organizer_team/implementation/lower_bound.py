


def lowerBound(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            ans = mid  # update the best result so far
            right = mid - 1  # search better result on the left side
        else:
            left = mid + 1  # search result on the right side
    return ans