

def A(x, y, k):
    if k >= 1000:
        return None
    if x == 0:
        #print("#k: ", k)
        ans = y + 1
    elif y == 0:
        #print("##k: ", k)
        ans = A(x - 1, 1, k+1)
    else:
        print("###k: ", k, "      ", "y = ", y)
        ans = A(x - 1, A(x, y - 1, k+1), k+1)
    return ans

if __name__ == "__main__":

    def test_ackerman():
        assert(A(0, 2, 1) == 3)
        assert(A(1, 2, 1) == 4)
        assert(A(2, 2, 1) == 7)
        assert(A(3, 2, 1) == 29)
    
    print(A(4, 1, 1))
   

    