## 문자열 - 그룹 애너그램

- `파이썬 알고리즘 인터뷰` 책을 바탕으로 정리한 내용입니다.  
- [리트코드 49번](https://leetcode.com/problems/group-anagrams/) 에서 풀어볼 수 있습니다.

### 문제설명

- 문자열 배열을 받아 애너그램 단위로 그룹핑하기
- Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
- Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

> 애너그램이란?
> 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.
> 'eat' 문자를 재배열하여 'tea', 'ate' 단어를 만들 수 있다.

### 풀이. 정렬하여 딕셔너리에 추가

- 책과 비슷하게 풀이했다! 
- 애너그램을 판단하는 가장 간단한 방법은 `정렬`하여 비교하는 것이다. 애너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖게 되기 때문이다.  
- `sorted()`는 문자열도 정렬가능하고 결과를 리스트 형태로 리턴한다.(`sort()`는 문자열 정렬불가) 이를 다시 딕셔너리 키로 사용하기 위해 `join()`으로 합친다. 
- 애너그램끼리는 같은 키를 갖게되고 value 리스트에 단어를 추가한다. 
- 마지막에 딕셔너리의 `values()`를 이용해 값만 추출하고 `list()`로 형변환해주어야 한다. 

[💾 소스코드 : solution.py](src/solution.py)

```python
def solution(strs):
    anagrams= collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())
```
