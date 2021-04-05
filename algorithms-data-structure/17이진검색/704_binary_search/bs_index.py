def search(nums: list[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1
        
nums = [-1,0,3,5,9,12]
print(search(nums, 9))
print(search(nums, 2))