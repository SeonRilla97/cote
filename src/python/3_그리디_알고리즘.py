# 모험가 길드

# N명 -> 공포도 증가 위험 대처 능력 감소
# 공포도 X면 -> 그룹의 모험가 수는 X이상 
# N 입력 -> N명의 공포도 입력

N = int(input())
result = list(map(int, input().split()))
result = sorted(result)

P = 0
groupCount = 0
while P < N:
    # 그룹 리더(공포도 젤 낮은 사람)
    value =result[P]

    # 남은 인원이 공포도 수 보다 작을 때
    if( P+value >= N):
        break
    # 공포도 만큼 인원 모집
    P =P + value
    #그룹 형성 
    groupCount+=1

print(groupCount)

# # 그룹 리더 (공포도가 가장 낮은 사람)
# for i in data:
#     count += 1
#     #그룹 결성의 경우 
#     if count >= i:
#         result +=1
#         count = 0
    
    
