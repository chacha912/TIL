def solution(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    answer = []
    for i in range(len(nums) - 2):
        print(i)
        if i > 0 and nums[i] == nums[i-1]:
            continue 
        l, r = i + 1, len(nums) - 1
        sum = nums[i] + nums[l] + nums[r]
        while l < r:
            print(l)
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else: 
                answer.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
    return answer
            

nums = [-1,0,1,2,-1,-4]
print(solution(nums))  # [[-1,-1,2],[-1,0,1]]
