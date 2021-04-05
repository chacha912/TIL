def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    # 전체 거리 안에서 n 개의 돌을 제거했을 때 최소 거리의 최댓값 answer를 찾는다
    # 즉, 전체 거리 내에서 이분탐색을 수행해 answer값을 찾는다. 
    # 최소거리 answer를 만족하기 위해 제거해야하는 돌의 개수가 
    # n보다 작거나 같으면 더 큰 범위에서, n보다 크다면 더 작은 범위에서 answer를 찾는다.

    left = 0
    right = distance 
    answer = 0

    while left <= right:
        rm_rock_cnt = 0
        prev = 0
        mid = (left + right) // 2
        for rock in rocks:
            if (rock - prev) < mid:
                rm_rock_cnt += 1
            else:
                prev = rock
        
        if rm_rock_cnt <= n:
            answer = mid 
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(solution(25, [2,14,11,21,17], 2)) # 4
print(solution(12, [2,4,6,8,10], 4)) # 6