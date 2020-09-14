def main():
    N = input()

    answer = int(N[0])
    for ch in N[1:]:
        if answer == 0 or ch == '0':
            answer += int(ch)
        else:
            answer *= int(ch)
    print(answer)

main()