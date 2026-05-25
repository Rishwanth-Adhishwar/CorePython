def prime_no(start, ending):
    for i in range(start, ending + 1):
        if i > 1:
            is_Prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_Prime = False
                    break
            if is_Prime:
                print(i, end=" ")

prime_no(1, 10)