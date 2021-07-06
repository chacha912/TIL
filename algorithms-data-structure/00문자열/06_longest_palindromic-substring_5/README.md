## 문자열 - 가장 긴 팰린드롬 부분 문자열

- `파이썬 알고리즘 인터뷰` 책을 바탕으로 정리한 내용입니다.  
- [리트코드 5번](https://leetcode.com/problems/longest-palindromic-substring/) 에서 풀어볼 수 있습니다.

### 문제설명

- 가장 긴 팰린드롬 부분 문자열을 출력하기
- Input: s = "babad"
- Output: "bab" or "aba"

### 풀이. 중앙을 중심으로 확장하기

- 리트코드에서 몇가지 접근법에 대한 설명이 나와있었다. 처음 문제를 봤을 때는 브루트 포스 방법밖에 생각이 안났다.
    - Approach 1: Longest Common Substring
    - Approach 2: Brute Force (시간복잡도 `O(n^3)`)
    - Approach 3: Dynamic Programming (시간복잡도 `O(n^2)`, 공간복잡도 `O(n^2)`)
    - Approach 4: Expand Around Center (시간복잡도 `O(n^2)`, 공간복잡도 `O(1)`)
    - Approach 5: Manacher's Algorithm (시간복잡도 `O(n)`)
- 책에서는 접근4. 중앙을 중심으로 확장하는 법으로 풀이를 했다. 투포인터가 슬라이딩 윈도우처럼 이동하며 팰린드롬인지 확인하는 풀이인데 먼저 읽어보고 혼자 다시 풀어봤다.
- 💡 예외처리의 중요성
    입력된 문자열이 한 글자이거나 전체가 팰린드롬인 경우에는 바로 리턴해줌으로써 전체적인 풀이 속도를 향상시킬 수 있다. 
- 💡 팰린드롬 체크하는 부분을 재귀 대신 반복을 사용하여 다음과 같이 깔끔하게 구현할 수 있었다. 시간도 더 짧아졌다. 
    ```python
    def checkPalin(left, right):
        while left >= 0 and right < L and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    ```
[💾 소스코드 : solution.py](src/solution.py)

```python
def solution(s):
    L = len(s)
    answer = ''

    def checkPalin(left, right):
        if left < 0 or right >= L:
            return s[left+1:right]
        if s[left] == s[right]:
            return checkPalin(left-1, right+1)
        return s[left+1:right]

    if L < 2 or s == s[::-1]:
        return s

    for i in range(L-1):
        even = checkPalin(i, i+1)
        odd = checkPalin(i, i+2)
        answer = max(answer, even, odd, key=len)
    
    return answer 
```

