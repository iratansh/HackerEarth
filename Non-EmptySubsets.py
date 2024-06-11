testCase = int(input())
while testCase > 0:
    N = int(input())
    arr = list(map(int, input().split()))
    K = min(arr)
    print(K)
    testCase -= 1
