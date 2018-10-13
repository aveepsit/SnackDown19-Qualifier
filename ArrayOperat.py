for testcase in range(int(input())):

    n = int(input())

    diff = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    for i in range(n):
        diff[i] = b[i] - diff[i]

    psbl = True

    for i in range(n-2):

        if(diff[i] == 0):
            pass
        elif diff[i]<0:
            psbl = False
            break
        else:
            chng = diff[i]
            #
            # a[i] += chng
            # a[i+1] += chng+1
            # a[i+2] += chng+2
            diff[i] -= chng
            diff[i+1] -= 2*chng
            diff[i+2] -= 3*chng

    if psbl and (diff[n-1]==0) and (diff[n-2]==0):
        print('TAK')
    else:
        print('NIE')
