text = 'this is book'
p = 'is'

def func(text,pattern):
    for i in range(len(text) - len(pattern) + 1): # text에서 p를 인덱스 에러에 걸리지 않고 얼마나 찾을 수 있는지
        for j in range(len(pattern)): # p의 각 텍스트를 비교해서 같은지 확인하는 루프 0번째 : 'i', 1번째 : 's'
            if text[i + j] != pattern[j]: # 같지 않으면 브레이크
                break
        else:
            return i
    return -1 # 끝까지 다 돌렸는데 없으면 -1 반환

print(func(text,p))


def func2(text, pattern):
    i = 0
    j = 0
    while j < len(pattern) and i < len(text):
        if text[i] != pattern[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == len(pattern):
        return i - len(pattern)
    else:
        return -1

print(func2(text,p))


def func3(text, pattern):
    m = len(pattern)
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+m] == pattern:
            return i
    return -1

print(func3(text,p))
