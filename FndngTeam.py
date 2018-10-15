for testcase in range(int(input())):

    n = int(input())
    dict = {}
    comb = 1
    m = (10**9)+7

    for x in input().split():
        no = int(x)
        try:
            dict[no] = dict[no] + 1
        except:
            dict[no] = 1
    dict = list(dict.items())
    dict.sort(key=lambda x: x[0], reverse=True)
    dict = [x[1] for x in dict]

    for ind in range(len(dict)):
        if dict[ind]==0:
            continue
        if (dict[ind]%2==0):
            for j in range(dict[ind]-1,2,-2):
                comb = (comb*j) % m
        else:
            for j in range(dict[ind],2,-2):
                comb = (comb*j) % m

            comb = (comb*dict[ind+1]) % m
            dict[ind+1] -= 1

    print(comb)
