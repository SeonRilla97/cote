# 탐욕법 (그리디) : 현재 상황에서 지금 당장 좋은 것만 고르는 방법


# N = N-1
# N / K

# N을 최대한 빨리 줄이기 (나눗셈 우선)
# 어떠한 수 N이 1일 될 때 까지 2가지중 한개 연산 선택, 연산의 수 구하기
# N에서 1빼기
# N을 K로 나누기 
N,K = map(int,input().split()) #  패킹 / 언패킹
count= 0
result = 0
while True:
    # 나눠 떨어지는 수로 바로 접근
    target = (N // K) * K
    result += (N - target)
    N = target

    # 더 나눠질 수 없을 때
    if N < K:
        break
    #나누고 count + 1
    result += 1
    N //=K

result += (N-1)
print(result)
