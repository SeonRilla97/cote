# 0~9
# 만들어질 수 있는 가장 큰 수 구하는 프로그램
# 입력받은 문자열을 자리수마다 + 또는 x 연산하여 가장 큰 수가 나오도록 한다.

data = input()


#입력받기
result = int(data[0])

for i in range(1, len(data)):
    num=int(data[i])
    if( num <= 1 or result <= 1):
        result+= num
    else:
        result*= num
# 1이하는 덧셈

# 나머지 곱셈

print(result)
