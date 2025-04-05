def add(a,b):
    result=a+b
    return result
def substract(a,b):
    result=a-b
    return result
def multiply(a,b):
     result=a*b
     return result
def divide(a,b):
    if b==0:
        return "zero is invalid in denominator"
    else:
        result=a/b
        return result
        
    
keysdict={"+":add,"-":substract,"*":multiply,"/":divide}
def calculator():
    
    a=int(input("Enter the first number\n"))
    while True:
        c=input("Select an operand +,-,*,/\n")
        if c in keysdict:
            b=int(input("enter b\n"))
            result=keysdict[c](a,b)
            print(f"Result:{result}")
        else:
            print("Invalid")
            continue
        print("if user wants to continue with the same number type y else type n to start a new")
        z=input()
        if z=="y":
            a=result
        else:
            a=int(input("Enter the new first value\n"))
calculator()
        

        

        
    
          
          
          
    
      


