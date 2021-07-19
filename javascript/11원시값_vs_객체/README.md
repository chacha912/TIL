# 원시값 vs 객체

원시타입(primitive type) | 객체타입(object/reference type)
:---:|:---:
단 하나의 값을 나타냄 | 다양한 타입의 값(원시값 또는 다른 객체)을 하나의 단위로 구성한 복합적인 자료구조
변경불가능한 값<br>(Immutable value)| 변경 가능한 값<br>(Mutable value)
변수(확보된 메모리 공간)에 실제 값이 저장됨 | 변수에 참조값이 저장됨
값에 의한 전달(pass by value)|참조에 의한 전달(pass by reference)

원시타입의 값, 즉 원시값은 변경 불가능한 값이다. 한 번 생성된 원시값은 읽기 전용(read only) 값으로서 변경할 수 업삳. 여기서 변경 불가능하다는 것은 변수가 아니라 `값`에 대한 진술이다. 변수는 언제든지 재할당을 통해 변수값을 변경(교체)할 수 있다. 상수는 재할당이 금지된 변수로, 단 한번만 할당이 허용되므로 변수값을 변경할 수 없다. 상수와 변경 불가능한 값을 동일시하는 착각을 할 수 있지만, 상수는 재할당이 금지된 변수일 뿐으로 아래 예시를 통해 확실히 알아본다.

```javascript

var a = 4;
a = 5; // var 키워드로 생성한 변수는 재할당이 가능하다.

const b = {name:'urim'};

b = {name:'cha'}; 
// Uncaught TypeError: Assignment to constant variable. 
// const 키워드로 생성한 변수는 상수로, 재할당이 불가능하다.

b.name = 'cha';
console.log(b);
// {name: "cha"}
// const 키워드를 사용해 선언한 변수에 할당한 객체는 변경가능(mutable)하다.
```