def prime_No_Print():
    for i in range(2,101):
        is_Prime=True
        for j in range(2,i):
            if i%j==0:
                is_Prime=False
                break
        if is_Prime:
            print(i,end=" ")

prime_No_Print()
