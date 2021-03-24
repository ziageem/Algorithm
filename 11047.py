#BAEKJOON 11047 동전

n,k=map(int,input().split())
coin=[]
for i in range(n):
  coin.append(int(input()))
coin.reverse()

count=0

for i in coin:
    count+=k//i
    k%=i
print(count)
