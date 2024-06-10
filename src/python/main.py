#정수형
a = 777
print(a)

#실수형
b=157.02
print(b)

#지수 표현 방식
c=1e9 # 10^9

#실수 값 연산 시 정확한 값이 나오지 않음을 주의
d= 0.3+0.6
print(d)
print(round(d,2))

# 나눗셈(/)의 결과는 실수형
# 나머지 연산자 (%)
# 몫 연산자 (//)
# 거듭제곱 (**)

#리스트 자료형
## 인덱싱 [ -값 , +값]
## 슬라이싱 a[1: 4] => index 1~3 조회
## 리스트 컴프리헨션
### append, sort, reverse, insert, count, remove
e = [1,2,3,4,5,6,7,8,9]
print(a)
f = [0] * 20 # 0이 20개인 리스트
print(f)

tmp_array=[i for i  in range(10)] # 1~9까지
tmp_arr=[i for i in range(20) if i % 2 == 1] # 1~19중 홀수만
tmp_array=[i*i for i  in range(10)] # 1~9 제곱
# tmp_array=[[0] * m for _ in range(n)] # N * M 크기 2차원 리스트
print(tmp_array)

n=3
m=4
array=[[0] * m for _ in range(n)]
x_array=[[0]* m ] * n #이렇게 하면 내부가 같은 객체로 인식한다
x_array[1][1]=5
print(x_array)
print(array)


a=[1,2,2,3,4,5,5,5]
remove_set= {3,5}
result=[i for i in a if i not in remove_set] 
print(result)


## 문자열 자료형
## 값 변경 불가
# "" / ''
a="hello"
b="World"
print(a+b)
print(a*3)
print(a[2:4])


## 튜플
#한번 선언된 값을 변경 불가
#서로 다른 성질 데이터 묶기 / 해싱의 키 값/ 메모리 효율적
a=(1,2,3,4,5)


## 사전
## Key : Value
## HashTable -> O(1)
## Keys() / Values()
data=dict()
data['사과']='Apple'
data['바나나']='Banana'
data['코코넛']='Coconut'


##집합
## 중복X / 순서 X
# 합 / 교 / 차 
# O(1)
# add, update, remove
data = set([1,2,3,4,5])
data2 = {1,2,3,4,4,4}


## 기본 입출력
#input / map 사용

#공백을 기준으로 구분된 데이터 입력
n=int(input())
arr=list(map(int, input().split()))
a,b,c = map(int,input().split()) #  패킹 / 언패킹

#입력 빠르게 받기
import sys
data = sys.stdin.readline().rstrip() # 개행 제거

## 출력
print( 7, end=" ")
print(f"정답은 {args}입니다.")


#조건문

# if 조건문:
#     실행문
# elif 조건문:
#     실행문
# else:
#     실행문

# 논리연산자 : and or not
# 기타 연산자 : in / not in [리스트,튜플,문자열,딕셔너리]


#반복문

# i = 1
# while i<9:
#     result+=i
#     i+=1
# print(result)

# for 변수 in 리스트:
#     실행문

# for i in range(1,10):
#     실행문

# continue / break



#함수

# def 함수명(매개변수):
#     실행문
#     return 반환값

# 함수 바깥 전역변수 사용 : global
# 함수 내 지역변수 vs 전역변수 => 내부가 우선
# 반환값 여러개 가능


# 람다 표현식

(lambda a,b : a+b)(3,7)

# 각각의 원소에 어떤 함수를 적용하기 위해 map을 사용한다.
# map(lambda a,b: a+b , list1, list2)



# 유용한 표준 라이브러리 
# 내장함수 
# itertools : 반복되는 데이터 처리 (순열, 조합)
# heapq : 힙 자료구조 (우선순위 큐)
# bisect : 이진 탐색 기능 
# collections : 덱, 카운터
# math : 수학적 기능 

sum([1,2,3,4,5])
min(7,3,5,2)
max(7,3,5,2)
eval("(3+5)*7")

sorted([9,1,8,5,4])
sorted([9,1,8,5,4], reverse=True)
array=[('A',35),('B',75),('C',50)]
sorted(array, key=lambda x: x[1], reverse=True) # Key 속성으로 정렬 기준 정의, 내림차순

#itertools

순열 : 순서 O , n개에서 서로다른 r개 nPr
조합 : 순서 x , n개에서 서로다른 r개  nCr

from itertools import product, permutations, combinations

data = ['A','B','C']

combinations(data,2)
permutations(data,2)
combinations_with_replacement : 중복 순열


#항목 별 개수 파악
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])



#수학
import math

# gcd 최대공약수

#최소공배수
def lcm(a, b ):
    return a*b // math.gcd(a,b)  #최대 공약수

