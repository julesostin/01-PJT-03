import sys

sys.stdin = open("_직사각형길이찾기.txt")

# 1) 문제 이해 15min
# - a,b,c의 세 변의 길이가 주어지고 나머지 한 변의 길이가 얼마인지 출력
# - a=4, b=3, c=4 의 입력을 받아서 d를 구하는 문제

# 2) 문제 접근 ...min
# - if문 써서 만약 a=b=c 같을때 d도 같고, 그렇지 않을 때는 d는 b와 같다.
# 


T = int(input())

for i in range(1, T+1):
    data = list(map(int, input().split()))

# 이것도 맞는지도 모르겠고..사실 왜 T+1을 하는지도^^; 
# 매번 SWEA풀때마다 테스트케이스에 +1하고 시작해서 쓰긴 헀는데..
# 