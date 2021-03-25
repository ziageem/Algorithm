#BAEKJOON 1931 회의실 배정

n=int(input())
arr=[]
for _ in range(n):
   a,b=map(int, input().split())
   arr.append((a,b))

#회의 종료시간 기준으로 정렬
arr=sorted(arr,key=lambda x:(x[1],x[0]))

count=1
prev=arr[0][1]
for i in arr[1:]:
  if prev<=i[0]:
    count+=1
    prev=i[1]

print(count)
