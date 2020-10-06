def solution(s):
    answer = len(s)

    for size in range(1, len(s)//2+1):
        seq = [s[i:i+size] for i in range(0, len(s), size)]
        cnt = 1
        temp = ""
        for i in range(len(seq)-1):
            if seq[i] == seq[i+1]:
                cnt += 1
                if i+1 == len(seq)-1:
                    temp += str(cnt) + seq[i]
                    break
            else:
                if cnt != 1:
                    temp += str(cnt) + seq[i]
                else:
                    temp += seq[i]
                cnt = 1
                if i+1 == len(seq)-1:
                    temp += seq[i+1]
        print(seq)
        answer = min(answer, len(temp))
                
        print(answer)
    return answer


solution(input())