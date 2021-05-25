## 문자열 - 가장 흔한 단어

- `파이썬 알고리즘 인터뷰` 책을 바탕으로 정리한 내용입니다.  
- [리트코드 819번](https://leetcode.com/problems/most-common-word/) 에서 풀어볼 수 있습니다.

### 문제설명

- 금지된 단어를 제외하고 가장 많이 등장한 단어를 출력하기
- 대소문자 구분하지 않고, 구두점(마침표, 쉼표 등)은 무시한다

### 풀이1. 스스로 풀어보기

- 처음에 들어온 입력값을 전처리하는 작업에서 고민을 했다. 대소문자 변환과 구두점 삭제를 해야하는데 저번 문제에서 사용했던 `re.sub` 정규식을 적용해보았다. 
- `max()`의 두번째 인자에도 key옵션을 주어 sort처럼 사용할 수 있었다. 

[💾 소스코드 : solution.py](src/solution.py)

```python
def solution(paragraph, banned):

    counts = collections.defaultdict(int)
    words = re.sub('[^a-zA-Z]', ' ', paragraph).lower().split()
    banned = set(banned)

    for word in words:
        if word not in banned:
            counts[word] += 1

    return max(counts, key=counts.get)
```
#### 💡 딕셔너리 `get()`, 최대 value에 대한 key 찾기

- 딕셔너리에서 키의 값을 가져올 때 대괄호방식과 get()방식이 있다. 
딕셔너리에 없는 키의 값을 가져오려고 시도할 때 `대괄호방식`은 에러를 발생하고 `get()`방식은 에러를 발생하지 않는다는 차이가 있다. 

    ```python
    >>> words = {'happy':3, 'home':7}
    >>> words['dog']

    Traceback (most recent call last):
    File "<pyshell#2>", line 1, in <module>
        words['dog']
    KeyError: 'dog'
    
    >>> words.get('dog') # 에러 발생 안함 
    ```

- `get(a,b)` 첫번째 인자 a에는 찾고싶은 key값을 입력하고, 두번째 인자 b에는 key가 없을 경우 출력할 값을 입력한다.
    ```python
    >>> words = {'happy':3, 'home':7}
    >>> words.get('dog', 'no exist')
    
    'no exist'
    ```
- 딕셔너리에서 최대 value에 대한 key를 찾는 법으로 `max(dict, key=dict.get)`를 사용할 수 있다. `max()`의 두번째 인자에 key값으로, key에 대한 value를 출력해주는 `dict.get`을 입력하면 value를 기준으로 최대값을 구해준다. 즉 `key= lambda x: a.get(x)`와 같다.

    ```python
    from collections import Counter
    a = Counter('abcdabbc')
    a # Counter({'b': 3, 'a': 2, 'c': 2, 'd': 1})
    max(a, key=a.get) # 'b'
    max(a, key= lambda x: a.get(x)) # 'b'
    ```

- 딕셔너리에서 최대 value에 대한 key를 찾는 법 2번째로 리스트컴프리헨션을 사용할 수 있다. `max(dict.values())`를 하게 되면 딕셔너리의 value 중에 최댓값을 출력해주며 `dict.items()`에서 k에 key값이 v에 value값이 반복되며 v가 value중 최대값일 때만 k를 출력하는 방법이다.

    ```python
    [k for k,v in a.items() if max(a.values()) == v] # ['b']
    ```
- 위의 두 방법은 최대값이 여러개일 때 차이가 있다. `max()`를 이용하면 value의 최댓값 중 맨 앞에 있는 key만 출력하고, `리스트 컴프리헨션`을 이용하면 value의 최댓값에 대한 모든 key를 출력할 수 있다.
    ```python
    a # Counter({'b': 3, 'a': 2, 'c': 2, 'd': 1})
    a['c']=3
    a # Counter({'b': 3, 'c': 3, 'a': 2, 'd': 1})
    max(a, key=a.get) # 'b'
    [k for k,v in a.items() if max(a.values()) == v] # ['b', 'c']
    ```

### 풀이2. 책 - 리스트 컴프리헨션, Counter 객체 사용

리스트컴프리헨션을 이용해 입력값 전처리를 한 번에 하고, Counter 모듈을 사용해 단어 개수를 처리하여 세 줄로 짧게 풀이를 했다. 

[💾 소스코드 : counter.py](src/counter.py)

```python
def solution(paragraph, banned):
    words = [word for word in re.sub('[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
```

#### 💡 `collections`모듈의 `Counter`클래스

- Counter 클래스는 `Counter([iterable-or-mapping])`로 사용하면 요소를 딕셔너리 `key`로, 요소의 개수를 딕셔너리 `value`로 저장하여 데이터의 개수를 셀 때 유용하다.
    ```python
    from collections import Counter
    Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    ```
- Counter 클래스는 데이터의 개수가 많은 순서로 정렬된 `배열`을 리턴하는 `most_common()` 메서드를 제공한다. 
    ```python
    from collections import Counter
    Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
    ```
- `most_common()`의 인자로 숫자 `k`를 넘기면 그 숫자만큼만 리턴하여, 가장 개수가 많은 k개의 데이터를 얻을 수 있다. 
    ```python
    from collections import Counter
    Counter('hello world').most_common(1) # [('l', 3)]
    ```

### 풀이3. 리트코드 - 정규식 안쓰고 문자열 전처리

- 정규식을 쓰지 않고 할 수 있지 않을까 고민했는데, 리트코드 풀이를 보니 가능했다. 
책과 같이 리스트 컴프리헨션을 사용하여 `isalnum()` 숫자 또는 문자일 때 `lower()` 소문자로 변환하여 저장하는 방법이었다. 여러가지 좋은 풀이를 보면서 배우는 점이 많다. 

- 금지 단어는 100개, `1 <= paragraph.length <= 1000`으로 주어져서 banned를 set으로 저장하고 word가 set안에 있는지 확인하면 O(1)로 찾을 수 있으니까 더 빠를 줄 알았는데 수가 크지 않아서 그런지 시간상 차이는 없었다. 

[💾 소스코드 : leetcode.py](src/leetcode.py)

```python
def solution(paragraph, banned):

    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
    words = normalized_str.split()
    word_count = collections.defaultdict(int)
    banned_words = set(banned)

    for word in words:
        if word not in banned_words:
            word_count[word] += 1

    return max(word_count.items(), key=lambda x: x[1])[0]
```

📚 참고사이트
[파이썬공식문서 Counter](https://docs.python.org/3/library/collections.html#collections.Counter)
[파이썬 collections 모듈의 Counter 클래스 사용법](https://www.daleseo.com/python-collections-counter/)