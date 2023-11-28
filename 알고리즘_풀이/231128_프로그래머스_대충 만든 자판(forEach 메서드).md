```python
# 프로그래머스 대충 만든 자판
def solution(keymap, targets):
    answer = []
    dic = dict()

    for key in keymap:
         for idx, k in enumerate(key):
            if k in dic and idx > dic[k]:
                continue
            dic[k] = idx

    for tar in targets:
        tmp = 0
        for t in tar:
            if t not in dic:
                tmp = -1
                break
            else:
                tmp += (dic[t] + 1)
        answer.append(tmp)
    return answer

["ABACD", "BCEFD"] ["ABCD", "AABB"] [9,4]
["ABCD"] ["ABDE"] [-1]
```

```js
// 프로그래머스 대충 만든 자판
function solution(keymap, targets) {
  const answer = [];
  const dic = {};

  keymap.forEach((key) => {
    key.split('').forEach((k, idx) => {
      if (dic[k] !== undefined && idx > dic[k]) {
        return;
      }
      dic[k] = idx;
    });
  });

  for (let i=0; i<targets.length; i++){
      let result = 0;
      for (let j=0; j<targets[i].length; j++){
          if (dic[targets[i][j]] === undefined){
              result = -1;
              break;
          } else {
              result += dic[targets[i][j]] + 1;
          }
      }
      answer.push(result)
  }

  return answer;
}
```

프로그래머스는 기본적으로 입력이 주어져서 그나마 편한듯?

### 자바스크립트

- 이중 for 문을 화살표 함수로 중첩하여 구현

- not in을 요소 === undefined로 해당 요소가 없다는 식으로 구현
  
  - in은 요소 !== undefined

- **forEach 메서드 = 배열.forEach(Current Value, Index, Array)**
  
  - Current Value : 순회하면서 처리할 현재 요소
  
  - Index : 현재 요소의 순번(인덱스)
  
  - Array : forEach 메서드를 호출한 배열 본인
  
  - 파이썬의 enumerate와 유사
