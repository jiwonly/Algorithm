import sys
input=sys.stdin.readline

# del : 인덱스로 삭제
# del 뒤에 한 칸을 띄고서 'del array[인덱스]' 형태로 사용
# 요소의 위치를 지정해서 삭제
# del str_list[3:]  # 여러개의 요소를 삭제

# remove() : 값으로 삭제

n=int(input())
candidate =int(input())
vote=list(map(int,input().split()))
result=[]
cnt=[]

for i in vote:
    if i in result:
        cnt[result.index(i)]+=1
    else:
        if len(result) >= n:
            idx=cnt.index(min(cnt))
            del result[idx]
            del cnt[idx]
        result.append(i)
        cnt.append(1)

result.sort()
print(' '.join(map(str,result)))