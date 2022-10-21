# n-queen problem
# 18013307 장은영 EunYoung Jang

print("Enter the number of queens( n >= 4 ) : ",end='')
queen = int(input())
total = 0

arr1 = [0 for _ in range(queen)]
arr2 = []
# Output1
def pos(k):
    # 같은 행에 존재하거나 대각선에 존재하면 False
    for i in range(k):
        if arr1[k] == arr1[i] or abs(arr1[k] - arr1[i]) == k - i:
            return False
    return True
def out1(k):
    global total
    if k == queen:
        total += 1
    else:
        for i in range(queen):
            arr1[k] = i
            if pos(k):
                out1(k+1)
out1(0)
print(total)
# Output2
def print_result(result):
    for i in range(queen):
        for j in range(queen):
            if j == arr2[i]:
                print('1', end=' ')
            else:
                print('0', end=' ')
        print()
    print()
def out2(n):
    global total
    if len(arr2) == queen:
        print_result(arr2)
        return
    for i in range(queen):
        if i not in arr2:
            mapped = True
            for j in range(len(arr2)):
                if i == arr2[j]-n+j or i == arr2[j]+n-j:
                    mapped = False
                    break
            if mapped:
                arr2.append(i)
                out2(n+1)
                arr2.pop()
for i in range(queen):
    arr2 = [i]
    out2(1)