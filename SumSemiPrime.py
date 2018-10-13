import math



#primes = set()
semiPrimes = set()

import math

def isSemiPrime(num):
    cnt = 0
    numCpy = num
    mlt = 1
    for i in range(2, num):
        if num % i == 0:
            mlt *= i
            num /= i
            cnt += 1
        while num % i == 0:
            num /= i
            cnt += 1
        if cnt >= 2:
            break

    if ((cnt == 2) and (mlt == numCpy)):
        semiPrimes.add(numCpy)
        return(True)
    else:
        return(False)




for testcase in range(int(input())):
    res = 'NO'
    n=int(input())
    for x in range(2,(n//2)+1):
        y = n-x
        if ((x in semiPrimes) or isSemiPrime(x)) and ((y in semiPrimes) or isSemiPrime(y)):
            res = 'YES'
            break

    print(res)
