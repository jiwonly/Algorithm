# 위상 정렬

import sys
from collections import deque
input=sys.stdin.readline

t=int(input()) # 테케 개수

for _ in range(t):
    n,k=map(int,input().split()) # 건물 개수, 건설순서 규칙 개수
    d=list(map(int,input().split())) # 각 건물당 건설에 걸리는 시간

    graph=[[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    dp = [0] * (n+1) # dp 이용
    q = deque()

    for i in range(k):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1

    w=int(input().strip()) # 건설해야할 건물 번호

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
            dp[i] = d[i-1]

    while q:
        now=q.popleft()

        for i in graph[now]:
            indegree[i]-=1
            dp[i]=max(dp[i],dp[now]+d[i-1])

            if indegree[i]==0:
                q.append(i)

    print(dp[w])




