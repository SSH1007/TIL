# Java Script

---

- VScode 환경에서 실행하기 위해 node.js를 설치한 뒤,   
  Code Runner라는 확장 프로그램을 설치했다.

- ctrl + alt + n으로 코드 실행 가능 

---

- 주석
  
  - 한 줄 주석 : // 주석
  
  - 여러 줄 주석 :   
    
    ```javascript
    /*
    여러줄 주석
    */
    ```
  
  ---
  
  # 변수

- 변수 정의 방법
  
  - const : 절대로 바뀌지 않는 상수, 수정 X, 대문자로 정의해라
  
  - let : 변경될 여지가 있는 값

- 변수 정의 주의점 5개
  
  - 변수는 문자와 숫자, \$와 \_만 사용 가능
  
  - 첫 글자는 숫자가 될 수 없음
  
  - 예약어는 사용할 수 없음
  
  - 가급적 상수는 대문자로 정의할 것
  
  - 변수명은 읽기 쉽고 이해할 수 있게 선언

--- 

# 문자형

```javascript
const name = "Miken"; // 문자형 string
const age = 30;

const name1 = "Mike";
const name2 = 'Mike';
const name3 = `mike`;

const message = "I'm a boy.";
const message2 = 'I\'m a boy.';

const message3 = `My name is ${name3}`;
console.log(message3) // My name is mike

const message4 = `나는 ${age+5}살 입니다.`;
console.log(message4) // 나는 35살 입니다.
```

- **\` ${표현식} `** 으로 표현식 표현 가능
  
  - 백틱(`)이 아니라 일반 따옴표로 감싸면 입력한 그대로 출력됨

- 문자열 + 문자열로 문자열 합치기 가능
  
  - 문자열 + 숫자로 할 경우, 숫자는 문자열로 변환된다.
  
  - ```javascript
    const name = 'Mike';
    const age = 5;
    
    console.log(name + age); // Mike5
    console.log(typeof(name + age)); // string
    ```

---

# 숫자형

```javascript
const age = 30;
const PI = 3.14;

console.log(1+2); // 3 더하기
console.log(10-3); // 7 빼기
console.log(3*2); // 6 곱하기
console.log(6/3); // 2 나누기
console.log(6%4); //2 나머지
```

- 숫자를 0으로 나눌 경우, Infinity가 나온다.

- 문자열을 숫자로 나눌 경우, **NaN(Not a Numver)** 가 출력됨

---

# Boolean형

```javascript
const a = true;
const b = false;

const name = 'Mike';
const age = 30;

console.log(name == 'Mike') // true
console.log(age > 40) // false
```

- 파이썬과 달리, **소문자**로 true, false가 나온다는 점에 주의

--- 

# null과 undefined

- Null은 값이 없다.

- undefined는 값이 할당되지 않았다.

--- 

# typeof 연산자

```javascript
const name = 'Mike';

console.log(typeof 3); // number
console.log(typeof name); // string
console.log(typeof true); // boolean
console.log(typeof "xxx"); // string
console.log(typeof null); // object
console.log(typeof undefined); // undefined
```

- null이 object로 나와있지만, 사실은 object(객체)가 아니다

---

---

# 대화 상자

```javascript
const name = prompt("이름을 입력하세요.","홍길동");
alert('환영합니다, ' + name + '님!')
alert(`환영합니다, ${name} 님!`)
const isAdult = confirm('당신은 성인입니까?');
console.log(isAdult);
```

- prompt (입력 받음)
  
  - prompt(질문, 기본값) 형태.
    
    - prompt()로 해도 값은 받아올 수 있음
  
  - 입력 대화 상자를 팝업시킨다.
  
  - prompt로 입력받은 정보는 무조건 **문자형**이다.

- alert (알려줌)
  
  - 사용자에게 정보를 보여줄 대화 상자를 팝업시킨다.
  
  - 확인 버튼 누르면 닫힌다.

- confirm (확인 받음)
  
  - true & false 값을 리턴하는 [확인][취소] 팝업 창을 띄운다.
  
  - 결제하시겠습니까? 정말 삭제하시겠습니까? 같이 확인을 하는데에도 사용한다.

- 기본 대화 상자의 단점
  
  - 팝업 발생 시 스크립트 일시 정지
  
  - 스타일링 불가

---

# Type Conversion(형변환)

- String() : 문자형으로 변환

- Number() : 숫자형으로 변환
  
  - /이나 \*은 문자형을 **자동 형변환**해준다.
    
    - "9080"/2 = 4540
  
  - Number('125adad') => NaN 반환
  
  - **true와 false는 각각 1과 0으로 반환**
  
  - **Number(null)은 0 반환**
  
  - **Number(undefined)는 NaN 반환**
  
  - 주의사항
    
    - Number(0)은 false지만, Number('0')은 true임
    
    - Number('')은 false지만, Number(' ')은 true임

- Boolean() : 불린형으로 변환
  
  - 숫자 0, 빈 문자열 '', null, undefined, NaN은 false 반환
  
  - 나머지는 true 반환

---

# 연산자(Operator)

- 연산 순위 : \*,/  >  +,1

- num = num + 1는 num += 1; 처럼 표현 가능

- \*\*는 거듭제곱

- %(나머지)는 홀짝을 구하거나, 범위 지정에도 사용 가능
  
  - n%2 = 1이면 홀수, n%2 = 0이면 짝수
  
  - 어떤 값이 들어와도 5를 넘기면 안되는 경우
    
    - x%5 = 0~4 사이의 값만 반환

- ++, --는 증가 연산자, 감소 연산자
  
  - ```javascript
    let num1 = 10;
    let result1 = ++num1;
    console.log(result1); // 11 반환
    
    let num2 = 10;
    let result2 = num2++;
    console.log(result2); // 10 반환
    ```

---

---

# 비교 연산자와 조건문

> #### >,  >=, <, <=, ==, !=

- 비교 연산자는 true나 false를 반환

- ==는 동등 연산자. 1=='1'은 true
  
  - ===는 일치 연산자. 1==='1'은 false (타입까지 비교)

## if문

```javascript
const age = 19;
if(age > 19){
  console.log('환영합니다');
} else if(age === 19) {
  console.log('수능 잘 보세요!')
} else {
  console.log('안녕히 가세요');
}
```

--- 

--- 

# 논리 연산자

### ||(OR)

- 여러개 중 하나라도 true면 true

- 즉, 모든 값이 false일때만 false를 반환

- 첫번째 true를 발견하는 즉시 평가를 멈추고 true 반환

### &&(AND)

- 모든 값이 true면 true

- 즉, 하나라도 false면 false를 반환

- 첫번째 false를 발견하는 즉시 평가를 멈추고 false 반환

- 가장 범위가 좁은 것부터 평가하는 것이 좋다.

- OR보다 우선 순위가 높다.

- ```javascript
  // 남자이고, 이름이 Mike이거나 성인이면 통과
  const gender = 'F';
  const name = 'Jane';
  const isAdult = true;
  
  if(gender === 'M' && (name === 'Mike' || isAdult)){
    console.log('통과')
  } else {
    console.log('돌아가.')
  } // 돌아가.
  ```
  
  - && 연산이 우선적으로 실행되기 때문에 괄호가 안 쳐지면 false || isAdult로 true 값이 반환되었음

### !(NOT)

- true면 false 반환

- false면 true 반환

```javascript
const age = prompt('나이가..?');
const isAdult = age > 19;

if(!isAdult){
  console.log('돌아가')
} // 5를 입력하면 '돌아가'가 출력
```

--- 

---

# Loop(반복문)

> ## for

```javascript
for (let i = 0; i< 10; i++){
  console.log(i)
} // 콘솔에 0~9를 출력.

/* 
for (초기값; 조건; 코드 실행 후 작업){
   반복할 코드
}
*/
```

- 조건이 false가 되면 멈춘다.

> ## while

```javascript
let i = 0;
while (i<10){
  console.log(i)
  i++;
} // 0~9까지 출력.
```

> ## do.. while

```javascript
let i = 0;
do{
  console.log(i)
  i++;
}while(i<10)
```

- 적어도 한번은 실행한다는 것이 while 문과의 차이점

> ## break, continue

- break : 멈추고 빠져나옴

```javascript
while(true){
  let answer = confirm('계속 할까요?');
  if(!answer){
    break;
  }
}
```

- continue : 멈추고 다음 반복으로 진행

```javascript
for(let i = 0; i<10; i++){
  if(i%2){
    continue;
  }
  console.log(i)
} // 0,2,4,6,8만 출력
```

--- 

--- 

# switch

```javascript
let fruit = prompt('무슨 과일을 사고 싶나요?')

switch(fruit){
  case '사과':;
    console.log('100원입니다.');
    break;
  case '바나나':
    console.log('200원입니다.');
    break;
  case '키위':
  case '멜론':
    console.log('300원입니다.');
    break;
  default:
    console.log('그런 과일은 없습니다')
}
```

- 보통 switch 문은 if문으로 대체가 가능함

--- 

--- 

# 함수(function)

> ### 함수 선언문

function 함수명(매개변수){  
  실행할 코드    

}

- 함수명(매개변수)로 호출 가능

- 재사용성 증가, 유지보수 쉬워짐

```javascript
function sayHello(name){  //(name = 'friend') 같이 디폴트 값을 설정가능.
  let msg = `hello`;
  if(name){
    msg = `hello, ${name}`;
    msg += ' ' + name;
  }
  console.log(msg);
}

sayHello(); // hello
sayHello('John'); // hello, John John
```

- 위 코드에서 msg는 지역변수이므로 함수 밖에서는 쓸 수 없음

- 전역변수로 선언하고 지역변수로 또 선언할 수 있음(각각 다르게 취급함)

- return이 없는 함수는 undefined를 반환한다.

- 함수에서 return은 결과 반환의 기능도 하지만, 강제 종료의 기능도 있다.

- 어디서든 호출 가능.  함수가 선언보다 위에 있어도 동작한다!

> ### 함수 표현식

```javascript
let sayHello = function(name = 'bro'){
  console.log(`Hello ${name}`);
}

sayHello(); // Hello bro
```

- 함수 정의 코드에 도달해야 비로소 함수가 생성됨

> ### 화살표 함수 (arrow function)

```javascript
let add = function(num1,num2){
  return num1 + num2;
};

let add1 = (num1,num2)=>{
  return num1 + num2;
};

let add2 = (num1, num2) => (
  num1 + num2
)
console.log(add(2,3)) // 5
console.log(add1(2,4)) // 6
console.log(add2(2,5)) // 7
```

- return이 한 줄짜리 짧고 간단한 형식이면 화살표 함수 형태로 변환할 수 있음

--- 

--- 

# Object

```javascript
const superman = {
  name : 'clark',
  age : 33,
}

console.log(superman.name) // clark
console.log(superman['age']) // 33
superman.gender = 'male';
console.log(superman.gender)  // male
superman['hairColor'] = 'black';
console.log(superman['hairColor'])  // black
delete superman.hairColor;
console.log(superman.hairColor)  // undefined
```

- 접근
  
  - 오브젝트.요소;
  
  - 오브젝트['요소'];

- 추가
  
  - 오브젝트.요소 = '값';
  
  - 오브젝트['요소'] = '값';

- 삭제
  
  - delete 오브젝트.요소;

--- 

## Object - 프로퍼티 존재 여부 확인

```javascript
const age = 33;
const superman = {
  name : 'clark',
  age,
}

console.log(superman.birthday); // undefined
console.log('birthDay' in superman); // false
console.log('age' in superman); // true
```

```javascript
function makeObject(name,age){
  return {
    name : name,
    age : age,
    hobby : 'football'
  }
}

const Mike = makeObject('Mike',30);
console.log(Mike); // 아래 참고.

console.log('age' in Mike); // true
console.log('birthday' in Mike); // false
```

- console.log(Mike)의 값은 

```javascript
{
  "name": "Mike",
  "age" : 30,
  "hobby" : "football"
}
```

로 나오며, 이는 Object(객체) 타입이다.  

```javascript
function isAdult(user){
  if (!('age' in user) || user.age < 20){
    return false;
  }
  return true;
}

const Mike = {
  name : "Mike",
  age : 30
};

const Jane = {
  name : "Jane",
};

console.log(isAdult(Mike)); // true
console.log(isAdult(Jane)); // false
```

--- 

## for ... in 반복문

```javascript
const Mike = {
  name : 'Mike',
  age : 30,
};

for (x in Mike){
  console.log(x,Mike[x]);
} // 'name' 'Mike'
// 'age' 30
```

--- 

--- 

# 객체의 method, this

```javascript
const superman = {
  name : 'clark',
  age : 33,
  fly : function(){
    console.log(`${this.name}가 날아갑니다`);
  }
}

superman.fly() // clark가 날아갑니
```

* method : 객체 프로퍼티로 할당된 함수
- this : 객체 내부의 요소를 메소드가 참조하기 위해 가지는 대상?

```javascript
let boy = {
  name : 'Mike',
  sayHello : function(){
  console.log(`Hello, I'm ${this.name}`);
  }
};

let girl = {
  name : 'Jane',
  sayHello : function(){
  console.log(`Hello, I'm ${this.name}`);
  }
};

girl.sayHello(); // Hello, I'm Jane
boy.sayHello(); // Hello, I'm Mike
```

- this는 호출된 시점, 즉 런타임에 결정된다.

- 화살표 함수는 일반 함수와는 달리 자신만의 this를 가지지 않음

- 화살표 함수 내부에서 this를 사용하면, **그 this는 외부에서 값을 가져옴** 

--- 

--- 

# 배열(Array)

let 배열 = ['요소0', '요소1', ... '요소n'];

- 인덱스로 접근 가능

- 배열[인덱스] = '새 값'; 으로 값 변경도 가능

- 배열은 문자열 뿐만 아니라, 숫자/객체/함수 등도 포함할 수 있음

```javascript
let arr = [
  '민수',
  3,
  false,
  {
    name : 'Mike',
    age : 30,
  },
  function(){
    console.log('Test');
  }
]
```

- 배열.length로 배열의 길이를 구할 수 있다.

- 배열 메소드
  
  - 배열.push(n) : 배열 끝에 n을 추가 (복수 가능)
  
  - 배열.pop() : 배열 끝 요소를 제거
  
  - 배열.unshift(n) : 배열 앞에  n을 추가 (복수 가능)
  
  - 배열.shift() : 배열 앞 요소를 제거

> ### for문과 for.. of 문

```javascript
let days = ['월','화','수'];
days.push('목');
days.unshift('일')

for (let index = 0; index < days.length; index++){
  console.log(days[index]);
}

for(let day of days){
  console.log(day)
}// for문보다 간단하지만 index는 모름
```

- 둘 다 '일', 월', '화', '수', '목'을 출력함
