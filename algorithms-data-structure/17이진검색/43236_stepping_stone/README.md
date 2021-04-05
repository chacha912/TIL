## 징검다리 - 이분탐색

- [프로그래머스 징검다리(level 4)](https://programmers.co.kr/learn/courses/30/lessons/43236) 에서 풀어볼 수 있습니다.

### 문제설명

- 출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성
- 제한사항
  - 도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
  - 바위는 1개 이상 50,000개 이하가 있습니다.
  - n 은 1 이상 바위의 개수 이하입니다.

### 문제풀이

- 전체 거리 안에서 n 개의 돌을 제거했을 때 최소 거리의 최댓값 answer를 찾는다  
   즉, 전체 거리 내에서 이분탐색을 수행해 answer값을 찾는다.
- 최소거리 answer를 만족하기 위해 제거해야하는 돌의 개수가  
   n보다 작거나 같으면 더 큰 범위에서, n보다 크다면 더 작은 범위에서 answer를 찾는다.

[💾 소스코드 : solution.py](src/solution.py)

```python
def solution(distance, rocks, n):

    rocks.sort()
    rocks.append(distance) # --1

    left = 0 # --2
    right = distance
    answer = 0

    while left <= right:
        rm_rock_cnt = 0
        prev = 0
        mid = (left + right) // 2

        for rock in rocks:
            if (rock - prev) < mid: # --3
                rm_rock_cnt += 1
            else:
                prev = rock # --4

        if rm_rock_cnt <= n: # --5
            answer = mid # --6
            left = mid + 1
        else:
            right = mid - 1

    return answer
```

1. 마지막 돌에서 끝까지의 거리도 포함해야 한다.
2. left 초기값으로 rocks[0]을 설정하면 안된다. 중간에 더 작은 사이거리가 있을 수 있다.
3. 돌과 이전 돌 사이의 거리가 mid(최소거리)보다 작다면, mid가 최소거리를 만족시킬 수 없으므로, 현재 돌을 제거해야한다. 따라서 제거해야하는 돌의 갯수를 하나 증가시킨다.
4. mid가 최소거리를 만족시킬 수 있다면, 돌은 그대로 남아있고 prev 위치를 현재 돌의 위치로 옮겨준다. 다음 돌은 현재 돌부터의 거리로 계산한다.
5. 제거해야하는 돌의 갯수가 n과 같을 경우에도, 구간의 최댓값을 찾기 위해 탐색을 계속한다.
6. 더 명시적으로 작성한다면, answer = max([answer, mid]) 로 쓸 수 있다.

#### 😲 느낀 점 & 배운 점

처음엔 여전히 이걸 어떻게 이분탐색으로 풀지? 하며 감을 못 잡고 있다가 풀이를 참고했다.
정말로 생각의 전환이 필요한 것 같다. 신기하다. 돌을 n개 만큼 없앨때 거리의 최솟값 중 최댓값을 구하는 문제를, 반대로 거리의 최솟값이 x일 때 몇 개의 돌을 없애야 만족하는지 조건을 바꾸어 생각하면 이분탐색으로 접근할 수 있다. 문제를 다 풀고 계속 보다보니 조금 감이 잡히는 것도 같다.
