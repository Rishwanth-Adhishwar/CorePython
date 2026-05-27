try:
    fh=open("ExceptionHanndling/test.txt",'w')
    try:
        fh.write("This is test file for exception Handling!!")
    finally:
        print("Going to close file")
        fh.close()
except(IOError):
    print("Error can't find the file to read data")
else:
    print("I will excute when no error occurs")
finally:
    print("I will execute always")