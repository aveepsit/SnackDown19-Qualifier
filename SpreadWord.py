for testcases in range(int(input())):
    n = int(input())
    sprd = [int(x) for x in input().split()]
    day = 1
    pre_i = 1
    i=1
    spread = sprd[0]
    while spread+i < n:
        pre_i = i
        day +=1
        i += spread
        spread += sum(sprd[pre_i:i])


    print(day)
