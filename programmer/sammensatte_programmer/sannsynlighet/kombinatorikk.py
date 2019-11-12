import sys

def ncr(n, r):
    """
    Beregner antall mulige uordnede utvalg
    uten tilbakelegging med størrelse r 
    individer fra en populasjon på n individer
    """
    if r == 0 and n == 0:
        return 1

    if n == 0 and r != 0:
        return 0


    T = 1
    N = 1
    try:
        for k in range(r):
            T = T*(n - k)
            N = N*(k + 1)
        return T/N
    except OverflowError:
        print("  ")
        print("  ")
        print("Overflow! The function ncr in kombinatorikk "+ \
            "cannot handle such large input n and r")
        print("Please try some smaller input")
        print("  ")
        raise
    
    return int(T/N)

def npr(n, r):
    """
    Beregner antall mulige ordnede utvalg uten
    tilbakelegging med størrelse r individer
    fra en populasjon på n individer
    """
    P = n
    for k in range(1, r):
        P = P*(n - k)
    return P
        

if __name__ == "__main__":

    
    assert ncr(0, 0) == 1
    assert ncr(1, 0) == 1
    assert ncr(0, 1) == 0
    assert ncr(1, 1) == 1

    assert npr(5, 4) == 5*4*3*2
    assert npr(10, 5) == 10*9*8*7*6
    assert npr(1200, 3) == 1200*1199*1198

    
    for i in range(1, 1000):
        try:
            assert ncr(i, 1) == i
        except AssertionError:
            print(f"error: got ncr({i}, 1) = {ncr(i, 1)}")
        
        try:
            k = i + 1
            assert ncr(k, 2) == int(i*(i + 1)/2)
        except AssertionError:
            print('got an error!')
            sys.exit(0)

    
    for i in range(int(1E10), int(1.00001E10)):
        try:
            assert ncr(i, 1) == i
        except AssertionError:
            print(f"error: got ncr({i}, 1) = {ncr(i, 1)}")
        
        try:
            k = i + 1
            assert ncr(k, 2) == int(i*(i + 1)/2)
        except AssertionError:
            print('got an error!')
            sys.exit(0)

    # ncr(7.5E9, 35) = 4.1E+305
    # r = 35 is largest possible r for this n
    print("%g" % ncr(int(7.5E9), 35))


    for k in range(19):
        # print some rows in pascals triangle
        for i in range(k + 1):
            print(ncr(k, i), end=' ')
        print(" ")


