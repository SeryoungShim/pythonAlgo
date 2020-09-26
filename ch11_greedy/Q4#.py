def main():
    N = int(input())
    # 오름차순 정렬
    lst = sorted(list(map(int, input().split())))
    target = 1
    for i in lst:
        if target < i:
            break
        else:
            target += i
    print(target)

main()