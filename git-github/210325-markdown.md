# How to use markdown

<strong style="color:orange; font-size:1.5em">1. 제목(#)</strong>

```markdown
# h1 제목(#)

## h2

### h3

#### h4

##### h5

###### h6
```

# h1 제목(#)

## h2

### h3

#### h4

##### h5

###### h6

---

<strong style="color:orange; font-size:1.5em">2. ul-li 순서 없는 리스트</strong>
hyphen(-), asterisks(\*), plus sign(+) 혼용 가능

```markdown
- Item
  - Item1
    - Item 1-1
    - Item 1-2
  * Item2
    - Item 2-1
  - Item3
```

- Item
  - Item1
    - Item 1-1
    - Item 1-2
  * Item2
    - Item 2-1
  - Item3

---

<strong style="color:orange; font-size:1.5em">3. ol-li 순서 있는 리스트</strong>

```markdown
1. Item1

   - Item 1-1

   * Item 1-2

2. Item2

   - Item 2-1

3. Item3
```

1. Item1

   - Item 1-1

   * Item 1-2

2. Item2

   - Item 2-1

3. Item3

---

<strong style="color:orange; font-size:1.5em">4. 문단 줄바꿈</strong>

```markdown
This is paragraph1.

This is paragraph2.

This is paragraph1.<br>
This is paragraph2.
```

This is paragraph1.

This is paragraph2.

This is paragraph1.<br>
This is paragraph2.

---

<strong style="color:orange; font-size:1.5em">5. 코드 Syntax highliting</strong>
`<pre>, <code>` : html 에서 소스코드 표현하기 위해 사용하는 태그로 변환

````markdown
```python
def print_status():
    print('md is so awesome!!')
```

In statements, use `backquote` to emphasize specific word.
````

```python
def print_status():
    print('md is so awesome!!')
```

In statements, use `backquote` to emphasize specific word.

---

<strong style="color:orange; font-size:1.5em">6. 링크</strong>

```markdown
[Google1](https://google.com)
[Google2](https://google.com "title 링크 설명")
[Google3][구글참조링크]

글 안에서 바로 쓴다면,

1. https://google.com 또는 <https://google.com> 주소 작성
2. a태그 이용 <a href='https://google.com'>Google4</a>
3. [구글참조링크] 바로 이용

[구글참조링크]: https://google.com "구글로 이동"
```

[Google1](https://google.com)
[Google2](https://google.com "title 링크 설명")
[Google3][구글참조링크]

글 안에서 바로 쓴다면,

1. https://google.com 또는 <https://google.com> 주소 작성
2. a태그 이용 <a href='https://google.com'>Google4</a>
3. [구글참조링크] 바로 이용

[구글참조링크]: https://google.com "구글로 이동"

---

<strong style="color:orange; font-size:1.5em">7. 이미지</strong>

```markdown
![대체텍스트(alternative text)](./1.png "이미지 설명 title")
<img src='./1.png' width='200' height=''>
[![대체텍스트(alternative text)](./1.png "이미지에 링크연결")](https://google.com)
```

![대체텍스트(alternative text)](./1.png "이미지 설명 title")
<img src='./1.png' width='200' height=''>
이미지 크기 조절 위해 img태그에 바로 속성 지정해도 좋음
[![대체텍스트(alternative text)](./1.png "이미지에 링크연결")](https://google.com)

---

<strong style="color:orange; font-size:1.5em">8. 강조</strong>

```markdown
_이탤릭체는_ _\* 또는 \_ 한개_
**두껍게는** **\*\* 또는 \_\_ 두개**
~~취소는~~ ~~\~\~ tilde 두개~~
<u>밑줄은 `<u></u>`태그 사용</u>
```

_이탤릭체는_ _\* 또는 \_ 한개_
**두껍게는** **\*\* 또는 \_\_ 두개**
~~취소는~~ ~~\~\~ tilde 두개~~
<u>밑줄은 `<u></u>`태그 사용</u>

---

<strong style="color:orange; font-size:1.5em">9. 수평선</strong>

```markdown
---
```

---

↑↑↑
hyphen(-), asterisk(\*), underscore(\_) 3개이상 쓰기

---

<strong style="color:orange; font-size:1.5em">10. 인용문 BlockQuote</strong>

```markdown
> 인용문

> 인용문 안에 인용문 (중첩)
>
> > 두번째 인용문
> >
> > > 세번째 인용문
```

> 인용문

> 인용문 안에 인용문 (중첩)
>
> > 두번째 인용문
> >
> > > 세번째 인용문

---

<strong style="color:orange; font-size:1.5em">11. 표</strong>

- 헤더 구분할때 3개이상의 hypen(-) 사용
- colon(:)으로 정렬방법 지정
  `:---`왼쪽정렬, `---:`오른쪽정렬, `:---:`중앙정렬
- 표 양 끝 vertical bar(|)는 생략 가능

```markdown
|   이름   |       나이 | 주소                     |
| :------: | ---------: | :----------------------- |
|  차유림  |         xx | 인천 xxxxxxxxxxxxxxxxxxx |
| 중앙정렬 | 오른쪽정렬 | 왼쪽정렬                 |
|          |       빈칸 |                          |
|   빈칸   |            |
|          |            | 빈칸                     |
```

|   이름   |       나이 | 주소                     |
| :------: | ---------: | :----------------------- |
|  차유림  |         xx | 인천 xxxxxxxxxxxxxxxxxxx |
| 중앙정렬 | 오른쪽정렬 | 왼쪽정렬                 |
|          |       빈칸 |                          |
|   빈칸   |            |
|          |            | 빈칸                     |
