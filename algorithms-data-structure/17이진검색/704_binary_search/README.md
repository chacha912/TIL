## 이진검색(Binary Search)

- `파이썬 알고리즘 인터뷰` 책을 바탕으로 정리한 내용입니다.
- [리트코드 704번](https://leetcode.com/problems/binary-search/) 에서 풀어볼 수 있습니다.

### 문제설명

- 정렬된 nums를 입력받아 이진검색으로 target에 해당하는 인덱스 찾기

### 풀이1. 재귀 풀이

절반씩 범위를 줄여나가며 맞출 때까지 계속 재귀 호출한다.  
[💾 소스코드 : bs_recursion.py](src/bs_recursion.py)

```python
def search(nums: list[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                return binary_search(mid+1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
        else:
            return -1

    return binary_search(0, len(nums) - 1)
```

### 풀이2. 반복 풀이

[💾 소스코드 : bs_while.py](src/bs_while.py)

```python
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1
```

### 풀이3. 이진 검색 모듈

파이썬에서 제공하는 biset 모듈을 사용한다.  
여러가지 예외 처리를 포함한 이진 검색 알고리즘이 깔끔하게 모듈 형태로 구현되어 있다.  
[💾 소스코드 : bs_bisect.py](src/bs_bisect.py)

```python
import bisect

def search(nums: list[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
```

#### 💡 파이썬 bisect 모듈

```python

```

~~bisect 모듈 사용법 추가~~

### 풀이4. 이진 검색을 사용하지 않는 index 풀이

리스트에서 해당 값의 인덱스를 찾아내는 index() 메소드를 사용한다.
해당 값이 존재하지 않는다면 ValueError가 발생한다.  
[💾 소스코드 : bs_index.py](src/bs_index.py)

```python
def search(nums: list[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1
```

### 풀이비교

4번째 풀이방법에서 index() 함수는 리스트의 앞에서부터 차례대로 값을 찾기 때문에,  
최악의 경우 O(N)의 시간이 소요되고, 뒤에 위치한 값일수록 점점 찾는 속도가 느려진다.

반면 이진검색은 항상 일정한 속도를 보인다.  
✔ **이진 검색의 시간복잡도는 O(logN)으로, 아무리 크기가 커도 속도 차이가 거의 없다.**

따라서 배열의 크기가 크고, 찾아야 하는 값이 항상 앞에만 있는 게 아니라면,
파이썬의 이진 검색 모듈인 bisect를 적극 활용해보자.  
(원래 bisect 모듈은 리스트의 삽입 지점을 찾는 모듈이지만,

| 풀이 | 방식                                 | 실행시간   |
| :--: | :----------------------------------- | :--------- |
|  1   | 재귀 풀이                            | 316 밀리초 |
|  2   | 반복풀이                             | 256 밀리초 |
|  3   | 이진 검색 모듈                       | 264 밀리초 |
|  4   | 이진 검색을 사용하지 않는 index 풀이 | 272 밀리초 |

#### 💡 이진 검색 알고리즘 버그

`mid = (left + right) // 2 `로 중앙의 위치를 구할 때,  
수학적으로 잘못된 점은 없으나 컴퓨터과학에서는 오버플로(overflow)가 발생할 수 있다.  
`left + right`가 자료형의 최댓값(int형일 경우, 2^32 - 1)을 넘어설 경우,  
C에서는 예상치 못한 결과가 나오고 자바에서는 오류가 발생한다.  
따라서 `mid = left + (right - left) // 2`를 이용하면 오버플로를 피하면서 정확한 mid값을 구할 수 있다.  
파이썬은 임의 정밀도 정수형을 지원하기 때문에 이 문제에서는 해당 사항이 없지만,  
자료형이 엄격한 언어들에서 발생할 수 있는 문제이기 때문에 주의할 필요가 있다.
