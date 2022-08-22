# atoi => 문자열을 숫자로
# itoa => 숫자를 문자열로
# (단 정수)

def atoi(S):
    dap = 0
    cnt = 0
    lenS = len(S)
    for s in S:
        dap+=(ord(s)-48)*10**(lenS-cnt-1)
        cnt+=1
    return dap

def atoi2(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i

def itoa(num):
    isPositive = True
    if num < 0:
        isPositive = False
        num = -num
    if num == 0:
        return '0'
    dap = ''
    while num:
        num, reminder = divmod(num, 10)
        dap = chr(reminder+48) + dap
    if isPositive:
        return dap
    else:
        return '-'+dap

print(atoi('123'), type(atoi('123')))
print(itoa(-123),type(itoa(123)))
print(atoi2('123'), type(atoi2('123')))
