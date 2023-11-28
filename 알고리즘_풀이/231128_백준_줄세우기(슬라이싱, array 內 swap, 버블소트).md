10431번 줄세우기

```python
P = int(input())
for p in range(1, P+1):
    cnt = 0
    lst = list(map(int, input().split()))[1:]
    end = len(lst) - 1
    while end > 0:
        last_swap = 0
        for j in range(end):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                cnt += 1
                last_swap = j
        end = last_swap
    print(p, cnt)
```

```javascript
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function F(P) {
  if (P <= 0) {
    rl.close();
    return;
  }

  rl.question('', (inputlst) => {
    let cnt = 0;
    const inputl = inputlst.split(' ').map(Number)
    const p = inputl[0]
    const lst = inputl.slice(1, );
    let end = lst.length - 1;
    while (end > 0) {
      let last_swap = 0;
      for (let j = 0; j<end; j++){
        if (lst[j] > lst[j+1]){
          [lst[j], lst[j+1]] = [lst[j+1], lst[j]];
          cnt ++;
          last_swap = j;
        }
      }
      end = last_swap;
    }
    console.log(p, cnt);

    F(P - 1);
  });
}

rl.question('', (inputP) => {
  const P = parseInt(inputP);
  F(P);
});
```

### 파이썬 -> 자바스크립트

- list(array)를 슬라이싱하는 방법
  
  - 파이썬 : lst[1:] 
    
    - 두번째부터 마지막 요소까지 슬라이싱
  
  - 자바스크립트 : const lst = input.slice(1, );
    
    - slice로 잘라내어 새로운 배열을 생성

- list(array) 안의 요소를 서로 뒤바꾸는 방법
  
  - 파이썬 : lst[j], lst[j+1] = lst[j+1], lst[j]
  - 자바스크립트 : [lst[j], lst[j+1]] = [lst[j+1], lst[j]];
  - 구조 분해 할당으로 배열의 속성을 해체하여 그 값을 개별 변수에 다시 담은 것이다.

- 테스트 횟수 T를 입력받고 T번 데이터를 입력받기
  
  - 자바스크립트는 테스트 횟수를 따로 입력받고 테스트 횟수를 인자로 하는 재귀함수를 돌려서 이를 구현한다. (비동기 방식이므로 이렇게 입력)
