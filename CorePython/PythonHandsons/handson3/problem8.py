def max(*numbers):
    max_value=numbers[0]
    
    for num in numbers:
        if num>max_value:
            max_value=num
    return max_value

r1=max(25,12,18,30)
r2=max(8,15,22,17,12)

print("Maximum of Four Numbers:",r1)
print("Maximum of Five Numbers:",r2)