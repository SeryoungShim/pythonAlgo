def main():
    N = int(input())
    lst = list(map(int, input().split()))
    lst = sorted(lst)

    cnt = 0
    i = -1
    j = 0
    while(i < len(lst) and j < len(lst)):
        while(j < len(lst)):
            if j - i >= lst[j]:
                cnt += 1
                i = j
                j += 1
                print(f"j : {lst[j]}")
                break
            else:
                j += 1
    print(cnt)

main()