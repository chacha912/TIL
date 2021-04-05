## 문자열 - 유효한 팰린드롬

- `파이썬 알고리즘 인터뷰` 책을 바탕으로 정리한 내용입니다.
- [리트코드 125번](https://leetcode.com/problems/valid-palindrome/) 에서 풀어볼 수 있습니다.

### 문제설명

- 주어진 문자열이 팰린드롬(회문)인지 확인
- 대소문자 구분하지 않고, 영문자와 숫자만 대상으로 함

> 팰린드롬(Palindrome) 이란 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 말합니다.
> 예) 소주 만 병만 주소

### 풀이1. 리스트로 변환

문자나 숫자일 경우에만 리스트에 추가하고 팰린드롬 여부를 판별한다.
[💾 소스코드 : palindrome_list.py](src/palindrome_list.py)

```python
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
```

#### 💡 파이썬 문자열 함수

|  문자열함수  | 설명                                                    | 사용법                              |
| :----------: | :------------------------------------------------------ | :---------------------------------- |
|   upper()    | 문자열을 대문자로 변경                                  | str.upper()                         |
|   lower()    | 문자열을 소문자로 변경                                  | str.lower()                         |
| capitalize() | 처음단어 대문자, 나머지단어 소문자로 변경               | str.capitalize()                    |
|  isupper()   | 대문자로 구성되어있으면 True, 아니면 False 반환         | str.isupper()<br>str[1:4].isupper() |
|  islower()   | 소문자로 구성되어있으면 True, 아니면 False 반환         | str.islower()<br>str[1:4].islower() |
|  isspace()   | 공백으로 구성되어있으면 True, 아니면 False 반환         | str.isspace()<br>str[1:4].isspace() |
|  isdigit()   | 숫자로만 구성되어있으면 True, 아니면 False 반환         | str.isdigit()<br>str[1:4].isdigit() |
|  isalpha()   | 문자로만 구성되어있으면 True, 아니면 False 반환         | str.isalpha()<br>str[1:4].isalpha() |
|  isalnum()   | 글자 또는 숫자로 구성되어있으면 True, 아니면 False 반환 | str.isalnum()<br>str[1:4].isalnum() |

~~다른 함수 추가~~

### 풀이2. 데크 자료형을 이용한 최적화

리스트의 **pop(0)** 시간복잡도는 O(N)  
데크의 **popleft()** 시간복잡도는 O(1)  
각각 n번씩 반복하면 리스트 구현은 O(N^2), 데크 구현은 O(N)으로 성능차이가 크다.
[💾 소스코드 : palindrome_deque.py](src/palindrome_deque.py)

```python
import collections

def isPalindrome(s: str) -> bool:

    # 자료형 데크로 선언
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
```

### 풀이3. 슬라이싱 사용

정규식으로 불필요한 문자를 필터링하고, 슬라이싱을 사용해 문자열을 조작한다.
[💾 소스코드 : palindrome_slicing.py](src/palindrome_slicing.py)

```python
import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1] # 슬라이싱
```

#### 💡 파이썬 정규표현식

- re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)

```python

```

~~정규표현식 메소드 추가~~

### 풀이비교

파이썬에서 제공하는 문자열 슬라이싱은 내부적으로 C로 빠르게 구현되어 있어 훨씬 더 좋은 속도를 기대할 수 있다.  
✔ **문자열 조작할 때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다.**  
문자열을 별도로 리스트로 매핑하는 등의 처리는 데이터 구조를 다루는 입장에서는 좋은 방법이지만, 별도 자료형으로 매핑하는 과정에서 상당한 연산 비용이 필요하므로 전체적인 속도에서는 오히려 손해를 볼 수 있다.

| 풀이 | 방식                        | 실행시간   |
| :--: | :-------------------------- | :--------- |
|  1   | 리스트로 변환               | 304 밀리초 |
|  2   | 데크 자료형을 이용한 최적화 | 64 밀리초  |
|  3   | 슬라이싱 사용               | 36 밀리초  |

#### 💡 파이썬 슬라이싱

| 슬라이싱 | 결과       | 해석                                                                                                              |
| :------- | :--------- | :---------------------------------------------------------------------------------------------------------------- |
| S[1:4]   | 녕하세     | 인덱스 1부터 4이전까지                                                                                            |
| S[1:-2]  | 녕하       | 인덱스 음수는 뒤에서부터 접근                                                                                     |
| S[1:]    | 녕하세요   | 시작 또는 끝은 생략 가능                                                                                          |
| S[:]     | 안녕하세요 | 사본을 리턴, **참조가 아닌 값을 복사하기 위해 사용** (문자열이나 리스트를 복사하는 파이썬다운 방식- Pythonic Way) |
| S[1:100] | 녕하세요   | 문자열 최대 길이만큼만 표현                                                                                       |
| S[-1]    | 요         | 마지막 문자(뒤에서 첫번째)                                                                                        |
| S[:-3]   | 안녕       | 뒤에서 3개 글자 앞까지                                                                                            |
| S[-3:]   | 하세요     | 뒤에서 3번째 문자에서 마지막까지                                                                                  |
| S[::1]   | 안녕하세요 | 세번째 자리는 step의미, 1은 기본값으로 동일                                                                       |
| S[::-1]  | 요세하녕안 | 문자열 뒤집기                                                                                                     |
| S[::2]   | 안하요     | 2칸씩 앞으로 이동                                                                                                 |
