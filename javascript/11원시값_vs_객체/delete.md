# 자바스크립트 delete 연산자

'delete 연산자를 사용하는 것이 왜 안티패턴인지'에 대한 러버덕 발표를 듣고, 수업시간에도 delete 연산자 관련 질문이 나와서 찾아본 내용을 정리했습니다.

## delete 연산자란?

연산자(operator)는 하나 이상의 표현식을 대상으로 연산을 수행해 `하나의 값`을 만드는 것입니다. 이 때 연산의 대상을 피연산자(operand)라 하고, 피연산자는 값으로 평가될 수 있는 표현식이어야 합니다.

delete 연산자는 객체의 프로퍼티를 삭제하는 부수효과를 가지며, 반환값은 `true`입니다. 단, 자바스크립트 비엄격모드에서 프로퍼티가 `non-configurable`일 경우 `false`를 반환합니다.(엄격모드일 때는 `false` 대신 `TypeError`가 발생합니다)
 
수업시간 질문은 delete 연산자로 삭제할 수 없는 프로퍼티도 있는가? 였고, 저의 궁금증은 반환값이 `false`인 경우는 어떤 경우일까? 였습니다.

## 문법

delete 연산자 구문은 다음과 같습니다. 여기서 expression, 표현식은 속성을 참조해야 합니다.  
 `delete expression`  

`object`는 객체의 이름, 또는 객체로 평가되는 표현식이고 `property`는 제거하려는 속성입니다.
`delete object.property`  
`delete object[property]`  

## delete 연산자 고려사항

### 1. 객체 속성을 삭제할 수 있는가? 

- 자바스크립트에서 객체의 속성을 삭제할 수 있는 유일한 방법입니다. 
- 존재하지 않는 속성을 삭제할 경우, 어떤 작업도 하지 않고 `true`를 반환합니다.
    ```javascript
    var Employee = {
        age: 28,
        name: 'abc',
    }

    console.log(delete Employee.name);   // true
    console.log(Employee);               // {age: 28}
    
    // 존재하지 않는 속성을 삭제하려하면 true를 반환
    console.log(delete Employee.salary); // true
    ```
- 객체의 프로토타입 체인에 같은 이름의 속성이 있다면, 삭제 후 오브젝트의 프로토타입 체인을 통해 속성을 사용할 수 있습니다. 즉, `delete`연산자는 자신의 프로퍼티만 삭제할 수 있습니다.
    // 이부분은 프로토타입 체인 학습 후 보충하겠습니다.
    ```javascript
    function Foo() {
        this.bar = 10;
    }

    Foo.prototype.bar = 42;

    var foo = new Foo();

    // Returns true, since the own property
    // has been deleted on the foo object
    delete foo.bar;

    // foo.bar is still available, since it
    // is available in the prototype chain.
    console.log(foo.bar);

    // We delete the property on the prototype
    delete Foo.prototype.bar;

    // logs "undefined" since the property
    // is no longer inherited
    console.log(foo.bar);       
    ```

### 2. 변수를 삭제할 수 있는가? 

delete 연산자는 객체의 속성을 삭제하는 것으로 변수를 삭제하지는 못합니다.  

- `var`로 선언한 속성은 글로벌 스코프나 함수 스코프에서 삭제할 수 없습니다.
    ```javascript
    var x = 1;
    delete x;         // false
    console.log(x);   // 1
    ```
    ```javascript
    function f() {
        var z = 44;
        delete z;     // false (함수스코프 지역변수)
    }
    ```
    - 오브젝트의 속성으로 있는 함수(메서드)인 경우는 삭제할 수 있지만, 글로벌 스코프의 함수를 삭제할 수 없습니다. 

- `let`, `const`로 선언한 속성은 어느 스코프에 정의되어 있든 삭제할 수 없습니다. 즉, var, let, const로 선언된 변수는 non-configurable 속성으로 구분되며, delete로 삭제할 수 없습니다.
    ```javascript
    var nameOther = 'XYZ';
    Object.getOwnPropertyDescriptor(window, 'nameOther');
    // {value: "XYZ", writable: true, enumerable: true, configurable: false}
    // 브라우저에서 var로 선언한 변수는 window 객체의 프로퍼티로 접근할 수 있습니다.

    delete nameOther;   // false
    ```

- 전역스코프에 선언된 프로퍼티(var, let, const 키워드를 사용하지 않고 선언하면 전역개체의 프로퍼티로 생성됩니다)는 configurable 하며 delete로 삭제할 수 있습니다.
    ```javascript
    adminName = 'xyz';
    EmployeeDetails = {
        name: 'xyz',
        age: 5,
        designation: 'Developer'
    };

    delete adminName;            // true
    delete EmployeeDetails.name; // true
    delete EmployeeDetails;      // true
    console.log(adminName);      // Uncaught ReferenceError: adminName is not defined
    ```

### 3. 배열 요소를 삭제할 수 있는가? 

자바스크립트에서 array는 객체로, 배열 요소 또한 delete 연산자를 사용해 삭제할 수 있습니다. 단,
배열객체에서 delete 연산자를 사용하여 배열 요소를 삭제하면 배열 안에서 요소는 삭제되지만, 배열을 재색인`reindex`하거나 배열의 길이가 변경되지는 않습니다. 따라서 배열 요소 삭제후 배열을 출력해보면, 해당 인덱스 자리가 `empty`로 출력되고, 인덱스에 접근해보면 `undefined`가 출력되고, 배열의 길이는 이전과 동일하게 출력됩니다. 즉, 배열요소를 delete 연산자로 삭제하면 프로퍼티(요소)는 삭제되지만 배열에 빈 자리가 남아있습니다. 
이때, Object.keys()를 출력해보면 해당 인덱스 key도 삭제된 것을 확인할 수 있습니다. 따라서 in 연산자(`prop in object`)를 사용했을 때도 `false`가 반환됩니다.  
따라서 배열 요소를 삭제할 때는 다음과 같은 방법을 추천합니다.

#### 3-1. undefined 값 할당하기
MDN에서는 배열요소가 삭제됐을 때 undefined 값으로 존재하기를 원한다면 delete연산자 대신 undefined 값을 할당하는 것을 제안하고 있습니다. 

```javascript
var trees = ['redwood', 'bay', 'cedar', 'oak', 'maple'];
delete trees[3];
if (3 in trees) {
    // 실행되지 않습니다.
}
```

```javascript
var trees = ['redwood', 'bay', 'cedar', 'oak', 'maple'];
trees[3] = undefined;
if (3 in trees) {
    // 실행됩니다.
}
```

#### 3-2. `pop()`, `shift()`, `splice()` 사용하기

### 4. built-in 객체를 삭제할 수 있는가? 

### 5. non-configurable 속성을 삭제할 수 있는가? 

`Non-configurable` 속성은 삭제할 수 없습니다. 
- Math, Array, Object와 같은 built-in objects의 속성은 내장되어 있는 정적 프로퍼티로 non-configurable 합니다. 
    ```javascript
    delete Math.PI; // false
    ```
- Object.defineProperty() 같은 메서드로 만든 non-configurable 속성도 삭제할 수 없습니다.
    ```javascript
    var Employee = {};
    Object.defineProperty(Employee, 'name', {configurable: false});

    console.log(delete Employee.name);  // false
    ```
아래 


📚 참고자료

[MDN - delete operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
[5 things you need to know about the delete operator in JavaScript](https://levelup.gitconnected.com/5-facts-about-delete-operator-in-javascript-c16fd2588cd)
[MDN - in operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)