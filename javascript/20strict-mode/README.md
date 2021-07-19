## strict mode란? 

ES5에서 도입된 자바스크립트 언어의 `문법을 좀 더 엄격히 적용`하여 오류를 발생시킬 가능성이 높거나 JS 엔진의 최적화 작업에 문제를 일으킬 수 있는 코드에 대해 `명시적인 에러 발생`시키는 모드를 말한다. ES6 에서 도입된 `클래스와 모듈`은 기본적으로 strict mode가 적용된다. 

## strict mode의 적용

전역의 선두 또는 함수 몸체의 선두에 `'use strict';`를 추가한다.
전역에 추가하면 스크립트 전체에 strict mode가 적용되고,
함수에 추가하면 해당 함수와 중첩 함수에 strict mode가 적용된다.
선두에 위치하지 않으면 동작하지 않는다. 

strict, non-strict mode를 혼용하여 사용하는 것 또한 오류를 발생할 수 있다.
strict mode는 즉시실행함수로 감싼 스크립트 단위로 적용하는 것이 바람직하다. 


## strict mode가 발생시키는 에러

1. 암묵적 전역
    선언하지 않은 변수를 참조하면 ReferenceError가 발생한다.

2. 변수, 함수, 매개변수의 삭제
    delete 연산자로 변수, 함수, 매개변수를 삭제하면 SyntaxError가 발생한다.

3. 매개변수 이름의 중복
    중복된 매개변수 이름을 사용하면 SyntaxError가 발생한다.

4. with 문의 사용
    with문을 사용하면 SyntaxError가 발생한다.

## strict mode 적용에 의한 변화

1. 일반함수의 this
    함수를 일반함수로 호출할 때 this에 전역객체가 아니라 `undefined`가 바인딩된다.
    생성자 함수가 아닌 일반 함수 내부에서는 this를 사용할 필요가 없기 때문이다. 

2. arguments 객체 
    매개변수에 전달된 인수를 재할당하여 변경해도 arguments객체에 반영되지 않는다. 
