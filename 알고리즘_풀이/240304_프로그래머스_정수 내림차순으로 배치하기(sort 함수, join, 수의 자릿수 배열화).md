## 프로그래머스. 정수 내림차순으로 배치하기

```python
def solution(n):
    answer = 0
    n = list(str(n))
    n.sort(reverse=True)
    answer = int(''.join(n))
    return answer
```

```javascript
function solution(n) {
    var answer = 0;
    const lst = [...n.toString()].map(Number);
    const slst = lst.sort((a,b)=>b-a);
    answer = parseInt(slst.join(''));
    return answer;
}
```

## 파이썬 -> 자바스크립트

- 정수 n을 **...** 로 개별 변수에 할당 후,  toString()을 걸어 문자열 배열로 변경.
  
  - 그 후 .map(Number)로 숫자로 바꿔준다.
  
  - 예) 1886 -> ['1', '8', '8', '6'] -> [1, 8, 8, 6]

- sort() 함수로 배열을 정렬해준다.
  
  - sort() 함수는 기본적으로 각 원소들을 **문자열** 형태로 변경하기 때문에, 
    [10, 8, 1]이 [1, 8, 10]이 아니라 ['1', '10', '8']로 정렬된다.
  
  - 따라서 숫자의 정렬을 하기 위해서는 매개변수를 이용한다.
    
    - lst.sort((a, b) => a-b); 오름차순
    
    - lst.sort((a, b) => b-a); 내림차순 

- 리스트.join(구분자);
  
  - 구분자는 생략할 경우, **`,`** 로 표기된다
  
  - `''`을 구분자로 하면 공백없이 하나의 문자열로 만든다.
