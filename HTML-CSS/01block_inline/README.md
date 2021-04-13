## HTML 블록레벨(Block level) 요소와 인라인(inline)요소

| 블록 요소                                    | 인라인 요소                               |
| :------------------------------------------- | :---------------------------------------- |
| div, h1, p                                   | span, img                                 |
| 사용 가능한 최대 가로 너비를 사용한다.       | 필요한 만큼(content)의 너비를 사용한다.   |
| 크기를 지정할 수 있다.                       | 크기를 지정할 수 없다.                    |
| width: 100%; height: 0; 으로 시작            | width: 0; height: 0; 으로 시작            |
| 수직으로 쌓인다.                             | 수평으로 쌓인다.                          |
| margin, padding 위,아래,좌,우 사용 가능하다. | margin, padding 위,아래는 사용할 수 없다. |
| 레이아웃 잡을 때 사용                        | 텍스트 다룰 때 사용                       |
| display: block;                              | display: inline;                          |

- 브라우저에서 default value 기본값은 width: auto; height: auto; 로 설정되어 있고 블록요소, 인라인 요소는 각각 위의 4번과 같이 동작한다.

## HTML 태그

####`<html>`

   ```html
   <html lang="ko">
     내용은 html 태그 안에서만 작성한다.
   </html>
   ```

   언어코드는 "ko", 국가코드 "kr" 과 다르다.
   언어코드는 [iso 639-1](https://ko.wikipedia.org/wiki/ISO_639-1_%EC%BD%94%EB%93%9C_%EB%AA%A9%EB%A1%9D) 에서 확인할 수 있다.
   <br>

####`<head>` `<body>`

   ```html
   <!DOCTYPE html>
   <html lang="ko">
     <head>
       문서의 정보
     </head>
     <body>
       문서의 구조
     </body>
   </html>
   ```

   html 작성하기 전, 최상단에 doctype 명시하여 브라우저가 html5 버전으로 출력할 수 있도록 한다.
   <br>

####`<head>` 내부

1. title 

   ```html
   <!DOCTYPE html>
   <html lang="ko">
     <head>
       <title>HTML 요소 레퍼런스</title>
       - 기타 정보
       - 스타일 직접 입력
       - 외부 스타일 연결
     </head>
   </html>

   <!DOCTYPE html>
   <html lang="ko">
     <head>
       - HTML 문서의 제목
       - 기타 정보
       - 스타일 직접 입력
       - 외부 스타일 연결
     </head>
   </html>
   ```

####`<body>` 내부

1. `<header>` `<footer>` 
    각각 헤더, 푸터 영역을 지칭하겠다는 의미
2. `<h1>`~`<h6>`
    - html은 구조를 담당. 주제, 제목 의미! 글자 크기 조절이 되지만 reset 하고 css로 정확하게 지정하기
    - h1 > h3 순서를 건너뛰어서 작성하지 말기, 내용을 찾고 목차 정리하는데 문제생길 수 있음
    - h1 은 한 페이지에 하나만 사용하기
3. `<main>`
    ie 에서 제한
4. `<article>`
    