#BAEKJOON 11399 ATM

n=int(input())
atm=list(map(int,input().split()))
atm.sort()
sum=0
for i in range(n):
    sum+=atm[i]*(n-i)
print(sum)
