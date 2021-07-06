def solution(nums):
    answer = [1]
    temp = 1
    for i in range(len(nums)-1):
        answer.append(answer[i]*nums[i])
    for j in range(len(nums)-1,-1,-1):
        answer[j] *= temp
        temp *= nums[j]
    return answer

nums = [1,2,3,4]
print(solution(nums))  # [24,12,8,6]
