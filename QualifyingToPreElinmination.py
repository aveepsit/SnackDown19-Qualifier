for cases in range(int(input())):
    [n,k] = [int(nk) for nk in input().split()]
    arr = [int(x) for x in input().split()][:n]
    arr.sort(reverse=True)
    if (k>=n) or (arr[n-1] == arr[k-1]):
        print(n)
    else :
        i=k-1
        while(arr[i]==arr[k-1]):
            i=i+1
        print(i)
