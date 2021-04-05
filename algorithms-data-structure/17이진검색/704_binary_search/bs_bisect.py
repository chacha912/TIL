import bisect

def search(nums: list[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1

nums = [-1,0,3,5,9,12]
print(search(nums, 9))
print(search(nums, 2))