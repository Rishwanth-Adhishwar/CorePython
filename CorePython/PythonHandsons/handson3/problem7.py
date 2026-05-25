def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b

def callback(operation,operand1,operand2):
    return operation(operand1,operand2)

r1=callback(add,10,20)
r2=callback(subtract,50,20)
r3=callback(multiply,5,4)

print("Add:",r1)
print("Subtract:",r2)
print("Multiply:",r3)
