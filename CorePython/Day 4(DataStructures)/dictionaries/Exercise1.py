def num_Str(n,dict_num):
    result=""
    for i in n:
        i=int(i)
        result+=(dict_num[i]+" ")
    return result

dict_num={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"Eight",9:"Nine"}

n=input("Enter a Number:")
print(num_Str(n,dict_num))



