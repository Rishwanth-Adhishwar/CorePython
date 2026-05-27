def set_c(sc):
    sc={x*x for x in range(1,n+1)}
    return sc

n=int(input("Enter no:"))
print(set_c(n))