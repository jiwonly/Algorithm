import sys
input=sys.stdin.readline
from collections import deque

# bfs 탐색
def bfs():
    queue = deque([[sz, sy, sx]]) # 괄호 주의
    dx=[1, -1, 0, 0, 0, 0] # 동 서
    dy=[0, 0, -1, 1, 0, 0] # 남 북
    dz=[0, 0, 0, 0, 1, -1] # 상 하

    while queue:
        z,y,x=queue.popleft() # pop : 스택, popleft : 큐

        if x == ex and y == ey and z == ez:
            return "Escaped in {0} minute(s).".format(visited[z][y][x])

        for i in range(6):
            nx= x + dx[i]
            ny= y + dy[i]
            nz= z + dz[i]

            # 범위 내에 있고 탐색하지 않았다면
            if 0<=nx<C and 0<=ny<R and 0<=nz<L and visited[nz][ny][nx]==0:
                # 탐색하는 곳이 금이 아니라면 탐색
                if graph[nz][ny][nx]=="." or graph[nz][ny][nx] == "E":
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    queue.append([nz,ny,nx]) # 괄호 주의

    return "Trapped!"


while True:
    L,R,C=map(int,input().split())

    if L == 0 and R == 0 and C==0 : break

    graph=[[] * R for _ in range(L)]
    visited=[[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    # 반복문 2번을 통해 3중 그래프 입력받기
    for i in range(L):
        for j in range(R):
            graph[i].append(list(map(str,input().strip()))) # strip: 양 쪽 공백 제거
        input() # 빈 줄 처리

    # 반복문을 통해 S와 E의 좌표 확인
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == "S":
                    sx,sy,sz=k,j,i
                elif graph[i][j][k] == "E":
                    ex,ey,ez=k,j,i

    print(bfs()) # 괄호 주의


