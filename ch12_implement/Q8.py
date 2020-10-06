def main():
    string = list(input())
    string = sorted(string)
    num = 0
    for index, ch in enumerate(string):
        if ch.isnumeric() == True:
            num += int(ch)
        else:
            print("".join(string[index:]) + str(num))
            break

main()