# ESLint

## 린트와 프리티어로 협업 환경 만들기

ESLint, Prettier로 여러명이 일관되게 코드 작업하는 법, 코드 규칙 자동화, 강제화

lint는 린트 롤러, 옷에 삐져나온 보프라기를 떼어낼 때 사용하는 것. 코드에도 보프라기가 있다. 

들여쓰기를 맞추지 않은 경우
선언한 변수를 사용하지 않는 경우
너무 긴 라인 등등..
이런 코드들이 작동하지 않는 건 아니지만
읽기 어렵고 유지보수하기 어렵게 만든다.

이런 코딩스타일과 잠재적인 오류, 버그를 검사하는 것이 린트이다

JSLint, JSHint, ESLint 가 있다.

코드 포매팅, 코드 품질
포매팅: 일관된 코딩 컨벤션을 유지하도록 하는 기능, 들여쓰기는 2칸으로 하라 등
품질: 잠재적인 오류나 버그를 미리 찾아주는 기능

## ESLint 설치

노드 패키지로 제공되어 npm 명령어로 설치
node.js 설치 
`npm install eslint`

기본 설정파일 요구
`touch .eslintrc.js`

.eslintrc.js 파일에 빈 객체를 만들어 노드 형식의 모듈을 생성
`module.exports = {}`

npm 스크립트에 lint 명령어 추가
package.json 파일에 추가
`"scripts":{"lint":"eslint src"},`

`npm run lint`로 실행

ESLint는 규칙이 있어야 그걸 보고 코드를 검사한다.
ESLint 홈페이지에 Rules에 가서 나와있는 규칙을 사용하면 된다.
https://eslint.org/docs/rules/

예로 하나 추가해보기 
.eslintrc.js 파일에서 추가

```js
    module.exports = {
        rules: {
            "no-unexpected-multiline":"error"
        }
    }
```
npm run lint 했을 때 에러메세지 안나오면 통과한 것 

## 자동으로 수정하기 

세미콜론을 중복으로 입력해도 잘 동작하지만 읽기 어려움 이걸 막는 규칙 추가
```js
    module.exports = {
        rules: {
            "no-unexpected-multiline":"error",
            "no-extra-semi":"error"
        }
    }
```

다시 돌려보면 에러가 나는데 `--fix` option으로 고칠수 있다고 나온다.
package.json 파일에서 명령어에 옵션 추가하기
`"scripts":{"lint":"eslint src --fix"},`

실행해보면 자동으로 코드를 수정해줌.

이렇게 ESLint 규칙중에는 수정가능한 것과 불가능한 것이 있다.
목록중에 왼쪽 렌치가 붙은것이 자동으로 수정할 수 있는 규칙이다.

## Extensible Config

왼쪽의 체크박스는, extends recommend 들이다.
eslintrc.js 파일에 설정해보기
그럼 체크박스 된 애들은 다 확인하는 것. 만약 이 설정 외에 더 필요하다면 rules 속성에 추가하기 

```js
    module.exports = {
        extends: [
            "eslint:recommended"
        ]
    }
```

## Prettier
프리티어는 코드를 더 이쁘게 만들어준다.
ESLint의 포맷팅과 겹치는 부분이 있지만
프리티어는 좀더 일관적인 스타일로 코드를 만들어준다. 
대신 코드 품질은 신경쓰지 않는다.

## 설치
프리티어도 npm 패키지이다
 
 `npm install prettier`
 설치 후 실행해보면 변경된 결과를 터미널에 출력한다.
 `npx prettier src/**/*`
 `npx prettier src/**/* --write`
 write 옵션을 주고 실행하면 코드가 바로 변경된다. 

프리티어는 eslint와 달리 규칙이 미리 세팅되어 있어 설정 없이도 바로 사용할 수 있다. 

## 포매팅

eslint는 max-len 규칙으로 코드만 검사한다.
프리티어는 코드를 자동으로 수정해준다. 
프리티어를 사용하면 코드의 `일관성`을 유지할 수 있다. 

## 통합방법
eslint를 사용해야 하는 이유
포맷팅을 프리티어에 맡기더라도 
코드 품질과 관련된 검사는 ESLint의 몫이기 때문

프리티어는 eslint와 통합하는 방법을 제공한다.
 eslint-config-prettier
 eslint-plugin-prettier

 프리티어 포매팅 규칙을 eslint로 추가하고
 충돌하는 옵션이 있으면 프리티어의 규칙을 우선하도록 한다.
  

`npm install eslint-config-prettier eslint-plugin-prettier`
설치 하고 설정파일에 설정 추가하기

```js
    module.exports = {
        extends: [
            "eslint:recommended",
            "plugin:prettier/recommended"
        ],
        env: {
            browser: true
        }
    }
```

## 자동화
매번 린트 명령어 실행하기 힘드니까 자동화하기
깃 훅 사용법/ 에디터 확장 도구 사용법
 
 1. 깃 훅 사용

 깃 훅을 이용해 변경한 코드만 검사 가능
 깃 명령어 실행 전후에 뭔가를 더 실행할 수 있는 방법이 깃 훅임
 `husky`를 함꼐 사용하면 수월하게 사용가능
 `npm install husky` 패키지 설치 후
 package.json 파일에 설정 추가
 ```json
 "husky: {
     "hooks": {
         "pre-commit": "echo \"이것은 커밋전에 출력됨\""
     }
 }
 ```

g c --allow-empty -m "빈 커밋" 실행해봄
잘 됨.
여기에 린트 명령어로 변경
```json
 "husky: {
     "hooks": {
         "pre-commit": "npm run lint"
     }
 }
 ```
g c --allow-empty -m "빈 커밋" 다시 실행해봄
커밋 직전에 린트가 실행되서 에러가 발생하면 커밋 취소함. 무조건 린트 통과해야 코드 커밋할 수 있음

만약 코드가 점점 많아지면 커밋이 느려질 수도 있음 .
커밋할때 변경된 파일만 린트로 검사하고 싶다면 `lint-staged`를 사용 
변경된, 스테이징된 파일만 린트를 수행하는 도구다. 

`npm install lint-staged` 패키지 설치
패키지 파일에 설정 추가
JS파일만 린트로 검사하기
pre-commit도 변경 
```json
 "husky: {
     "hooks": {
         "pre-commit": "lint-staged"
     }
 },
 "lint-staged": {
     "*.js": "npm run lint"
 }
 ```

2. 에디터 확장도구
코딩할 때 바로 검사하기
vs-code의 eslint나 프리티어 익스텐션 활용하기

프리티어 규칙을 ESLint에 통합했기 때문에 ESLint 익스텐션만 설치해봄

eslint 설치 
설정파일에서 익스텐션 설정 추가
settings.json

`{"eslint.enable": true}`

코드에서 바로 빨간 줄로 보여준다. 
시각적으로 훨씬 좋다. 
에디터 설정중에 저장할 때 코드를 다 고쳐주는 옵션도 있다. 

```json
{
    "eslint.enable": true,
    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true
    }
}
```       

