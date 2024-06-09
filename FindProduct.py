array = int(input())
split_array = input().split()
answer = 1 
for el in split_array:
    answer = answer * int(el)
print(answer%(10**9+7))
