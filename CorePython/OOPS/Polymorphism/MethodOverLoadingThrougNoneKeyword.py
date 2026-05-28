class Example:
    
    def Method_OverLoad_None(self,a,b=None):
        if b is None:
            print(f"Single argument:{a}")
        elif isinstance(a,int) and isinstance(b,int):
            print(f"Two Integers:{a},{b}")
        elif isinstance(a,str) and isinstance(b,str):
            print(f"Two Strings:{a},{b}")
        else:
            print(f"Mixed tyoes:{a},{b}")
            
obj=Example()
obj.Method_OverLoad_None(1)
obj.Method_OverLoad_None(1,2)
obj.Method_OverLoad_None("Hello","Rishwa")
obj.Method_OverLoad_None("hi",9)
            
            