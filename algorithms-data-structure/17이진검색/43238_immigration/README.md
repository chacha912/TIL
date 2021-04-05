## 입국심사 - 이분탐색

- [프로그래머스 입국심사(level 3)](https://programmers.co.kr/learn/courses/30/lessons/43238) 에서 풀어볼 수 있습니다.

### 문제설명

- 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성
- 제한사항
  - 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
  - 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
  - 심사관은 1명 이상 100,000명 이하입니다.

### 문제풀이

- `[left, right]` 시간에서 심사최대인원을 만족하는 최소 시간을 이분 탐색으로 구한다.
- `left = 1, right = 가장 오래 걸리는 심사관이 모든 사람을 심사하는 시간` 을 초기값으로 설정한다.
- 현재 시간(mid)에 각 심사관들이 심사할 수 있는 최대 인원을 모두 합한 값과 주어진 입국심사 기다리는 사람수를 비교한다.

> 🗝 **Tip**
> 이분탐색 문제는 제한사항에 주어지는 숫자가 굉장히 크고
> 최댓값 또는 최솟값을 구하는 경우가 많다고 한다.

[💾 소스코드 : solution1.py](src/solution1.py)
[💾 소스코드(강사님) : solution2.py](src/solution2.py)

```python
def solution(n, times):
    answer = float('inf')  # --1
    left = min(times) # --2
    right = max(times) * n # --3

    def get_people(maxTime, timeArr):
        maxPeople = 0
        for time in timeArr:
            maxPeople += maxTime // time
        return maxPeople

    while left <= right: # --5
        mid = (left + right) // 2
        totalPeople = get_people(mid, times)
        if totalPeople >= n: # --4
            answer = min([answer, mid])
            right = mid - 1
        else:
            left = mid + 1

    return answer
```

1. 처음 answer는 `float('inf')` 무한대 값으로 명시적으로 할당하였다.
2. left 값은 `min(times) * n` 보다 작은 경우 있을 수 있으므로 n 곱하지 않는다.
3. 최댓값, 최소값만 구할경우 sort()함수 사용하지 않아도 가능하다.
4. totalPeople 이 n 과 같을 때에도 다시 한번 right를 범위를 줄여서 탐색해야한다.  
   최대 심사 인원수가 6명 구간의 최소값을 구해야 하므로!
5. left 와 right 가 같을 때도, totalPeople 값 확인해야한다.  
   (마지막에 left, right, mid가 모두 같을 경우의 값 확인)

#### 😲 느낀 점 & 배운 점

처음 혼자 문제를 풀어보려고 했을 때는, 이진 검색임을 알았음에도 어떻게 적용해야할지 모르고  
naive하게 접근했었다. 이쪽 심사관 자리가 비었는데 저쪽으로 가야하나..? 라는 고민을 하던 중  
강사님께서 몇 가지 힌트를 주셨고, 아하! 이렇게 푸는 거였구나 하면서 신나게 코드를 짜다가  
또 몇가지 문제들로 시간초과 발생...! 두영님이랑 얘기하면서 코드를 고쳐나갔는데 신기하고 재밌었다.

> **💡 다음에 조심해야 할 부분 메모**
>
> - 함수명, 변수명 명시적으로 정하기 get_people()
> - 불필요한 데이터를 생성하여 공간 낭비하지 않기
> - if 문에서 값 비교할 때, 함수계산이 오래 걸린다면 한번만 계산하고 변수에 할당하여 값을 넘겨주기
