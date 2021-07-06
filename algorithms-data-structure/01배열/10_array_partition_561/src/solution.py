def solution(nums):
    return sum(sorted(nums)[::2])

nums = [1,4,3,2]
print(solution(nums))  # 4