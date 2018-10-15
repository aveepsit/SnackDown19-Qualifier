ncrLib = {}

def nc2(n):
    c = (n*(n-1))//2
    ncrLib[n] = c
    return c

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
        while dict[ind]>0:
            if dict[ind]>1:
                try:
                    comb = (comb * ncrLib[dict[ind]])%m
                except:
                    comb = (comb * nc2(dict[ind]))%m
                dict[ind] -= 2
            else:
                comb = (comb * dict[ind+1])%m
                dict[ind+1] -= 1
                dict[ind] = 0

    print(comb)
