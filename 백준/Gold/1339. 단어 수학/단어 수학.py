import sys
from collections import deque
input=sys.stdin.readline

# 자릿수가 크다고 해서 높은 숫자로 바꾸면 안됨

n=int(input())
words = [input().strip() for _ in range(n)]

# 딕셔너리
weight={}

# 1. 각 알파벳의 가중치 계산
for word in words:
    p=1
    for i in word[::-1]:
        if i in weight:
            weight[i] += p
        else:
            weight[i] = p
        p*=10

# {'F': 1, 'C': 1010, 'G': 100, 'B': 1, 'E': 10, 'D': 100, 'A': 10000}

# 2. 가중치가 높은 순서대로 정렬
# weight.items()는 딕셔너리의 (키, 값) 쌍을 튜플로 묶어서 반환
# 예: [('A', 123), ('B', 45), ...]
# key=lambda x: x 은 정렬 기준을 지정
sorted_weight=sorted(weight.items(), key=lambda x: x[1], reverse=True)

# 3. 9부터 차례대로 할당
num=9
alpha_to_num = {}
for i, j in sorted_weight:
    alpha_to_num[i] = num
    num-=1
    
# 4. 실제 숫자로 변환하여 합산
result=0
for word in words:
    val=0
    for i in word:
        val=val*10+alpha_to_num[i]
    result+=val

print(result)