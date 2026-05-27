class Error(Exception):
    pass
class ValueToSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass

num=10
while True:
    try:
        i=int(input("Enter No:"))
        if i<num:
            raise ValueToSmallError
        elif i>num:
            raise ValueTooLargeError
        break
    except ValueToSmallError:
        print("Value too small,try again!")
    except ValueTooLargeError:
        print("Value too large,try again!")
print("Congrats, You Won Guessed Correctly")
        