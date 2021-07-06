def solution(nums, target):
    map = {}
    for i, v in enumerate(nums):
        if target - v in map:
            return [map[target-v], i]
        map[v] = i
    return -1
    
nums = [2,7,11,15]
target = 9

print(solution(nums, target))