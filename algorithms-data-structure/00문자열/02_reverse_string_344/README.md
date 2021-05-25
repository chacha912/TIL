## 문자열 - 문자열 뒤집기

- `파이썬 알고리즘 인터뷰` 책을 바탕으로 정리한 내용입니다.  
- [리트코드 344번](https://leetcode.com/problems/reverse-string/) 에서 풀어볼 수 있습니다.

### 문제설명

- 문자열을 뒤집는 함수 작성하기  
- 입력값은 문자배열이며, 공간복잡도 O(1)로 리스트 내부를 직접 조작하기  
- `1 <= s.length <= 10^5`  
> Do not allocate extra space for another array. 
> You must do this by modifying the input array in-place with O(1) extra memory.

### 풀이1. 투포인터를 이용한 스왑

투포인터 풀이는 단어 그대로 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식이다.  
이 문제에서는 포인터를 점점 범위를 좁혀가며 스왑하는 형태로 조작한다.  
[💾 소스코드 : reverse_two_pointer.py](src/reverse_two_pointer.py)

```python
def reverseString(s):
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)
```

### 풀이2. `Pythonic way`

입력값이 리스트로 제공되면 reverse() 또는 문자열 슬라이싱을 이용해 한 줄로 쉽게 풀이할 수 있다. 

방법 | 대상
:--:|:--:
reverse()| 리스트
문자열 슬라이싱 | 문자열, 리스트

[💾 소스코드 : pythonic.py](src/reverse_pythonic.py)

```python
def reverseString(s):
    # s.reverse()
    # s = s[::-1]
    s[:] = s[::-1]
    print(s)
```

#### 💡 `s = [s::-1]` vs `s[:] = s[::-1]`

- 문자열에서는 인덱스에 접근해 값을 변경할 수 없다. (리스트는 가능)   
    `str = 'abcd'`  
    `str[0] = 'c'`  TypeError: 'str' object does not support item assignment

- 리스트에서 `s = s[::-1]`을 사용할 경우, 새로 리스트를 만들기 때문에 공간복잡도를 O(1)로 제한하는 문제에서 오류가 발생한다.  
    ```python
    str = ['h','e','l','l','o']
    print(id(str), str) # 2048010173952 ['h', 'e', 'l', 'l', 'o']
    str = str[::-1]     # str[::-1] 에 해당하는 값을 메모리 공간에 저장후 할당한다.
    print(id(str), str) # 2048010174080 ['o', 'l', 'l', 'e', 'h']
    ```

- 리스트에서 `s[:] = s[::-1]`을 사용하면 원래 있던 값을 변경하므로 공간복잡도 O(1)로 해결가능하다.
    ```python
    str = ['h','e','l','l','o']
    print(id(str), str) # 1845919169984 ['h', 'e', 'l', 'l', 'o']
    str[:] = str[::-1]     
    print(id(str), str) # 1845919169984 ['o', 'l', 'l', 'e', 'h']
    ```


### 풀이비교

| 풀이 | 방식                        | 실행시간   |
| :--: | :-------------------------- | :--------- |
|  1   | 투포인터 이용한 스왑            | 216밀리초 |
|  2   | 파이썬다운 방식 | 208 밀리초  |
