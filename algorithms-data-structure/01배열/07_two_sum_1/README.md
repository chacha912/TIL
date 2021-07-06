## 배열 - 두 수의 합

- `파이썬 알고리즘 인터뷰` 책을 바탕으로 정리한 내용입니다.  
- [리트코드 1번](https://leetcode.com/problems/two-sum/) 에서 풀어볼 수 있습니다.

### 문제설명

- 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
- Input: `nums = [2,7,11,15], target = 9`
- Output: `[0,1]`

### 풀이1. 브루트 포스로 계산

- 하나씩 다 해보는 브루트 포스로 풀이할 경우 O(N^2) 이 소요된다.

[💾 소스코드 : solution.py](src/solution.py)

```python
def solution(strs):
    anagrams= collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())
```
