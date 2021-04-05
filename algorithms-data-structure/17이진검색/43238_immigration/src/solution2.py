def solution(n, times):
    answer = float('inf') 
    left = min(times) 
    right = max(times) * n 

    def get_people(maxTime, timeArr):
        maxPeople = 0
        for time in timeArr:
            maxPeople += maxTime // time 
        return maxPeople

    while left <= right:
        mid = (left + right) // 2 
        totalPeople = get_people(mid, times)
        if totalPeople >= n:
            answer = min([answer, mid])
            right = mid - 1
        else:
            left = mid + 1

    return answer

print(solution(6, [7, 10])) # 28