def ChkPrime(No):
    flag = True
    for i in range(2, int(No / 2 + 1)):
        if No % i == 0:
            flag = False
            break
    return flag
