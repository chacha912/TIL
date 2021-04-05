def solution(n, times):
    answer = 0
    left, right = 0, n * 1000000000

    while left <= right: 
        mid = (left + right) // 2
        maxPeople = 0
        for i in times:
            maxPeople += mid // i 
        if maxPeople >= n:
            right = mid - 1
        elif maxPeople < n:
            left = mid + 1

    answer = right + 1
    return answer

print(solution(6, [7, 10])) # 28