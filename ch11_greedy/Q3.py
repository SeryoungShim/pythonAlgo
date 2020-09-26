def main():
    lst = list(map(int, input()))
    # 0으로 바꾸기
    to_zero = 0
    # 1로 바꾸기
    to_one = 0
    
    if lst[0] == 0:
        to_one = 1
    else:
        to_zero = 1

    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            if lst[i+1] == 0:
                to_one += 1
            else:
                to_zero += 1
    print(min(to_zero, to_one))

main()