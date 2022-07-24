# 알고리즘 문제 풀 때 팁

---

- [x] input()보다 빠르게 입력값 받기   

```
import sys
input = sys.stdin.readline()    
```

- dap = input()으로 받았을 경우, dap.rstrip()으로 idle 같은 인터프리터에서 입력했을 때 엔터를 눌러 생기는 \n을 제거해줘야 한다.  

---

- [x] 정규 표현식으로 숫자나 알파벳 걸러내기

```
import re
S = input()
s = re.sub("[0-9]+","",S)  # 0~9까지의 숫자 여러개들을 ""로 치환
s = re.sub("[^a-zA-Z., ]","",S)  # a-z,A-Z,온점,쉼표,스페이스를 ""로 치환 
```

--- 

- [x] sorted()로 정렬

```
tc = ['abc','abdva','zfvd','zdv','egexvxv']
tc = sorted(tc)
['abc', 'abdva', 'egexvxv', 'zdv', 'zfvd']
# 알파벳 순으로 정렬됨

tc = sorted(tc,key=lambda x:len(x))
['abc', 'zdv', 'zfvd', 'abdva', 'egexvxv']
# 정렬된 상태에서 다시 단어의 길이로 정
```

--- 

- [x] print()에서 소수점 출력

```
su = 1.2586125
print('%.5f'%su)  # 소수점 5자리까지 출력(반올림 같은거 없음)
print(f'{su:.5f}')  # 동
```

---

- [x] 딕셔너리 value 값으로 key 값 찾아야 할 때

- for문과 if 딕셔너리[key] == value:로 찾아도 되나, 시간 복잡도 O(n) 이상이 될 수 있음

- 차라리 딕셔너리를 만들 때, value가 key고 key가 value인 **역 딕셔너리**를 하나 더 만들면 O(1)로 작업 가능

---

- [x] for문에서 거꾸로 range 돌기

```
for i in range(len(N)):
    print(N[(len(N)-1-i])
```

--- 

tbd
