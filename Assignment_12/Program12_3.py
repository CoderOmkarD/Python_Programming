def Arithmatic(No1,No2):
    Add=No1+No2
    Sub=No1+No2
    Div=0
    
    Mult=No1*No2
    print("Addition is ",Add)
    print("Multiplication is ",Mult)
    try:
        Div=No1/No2
    except ZeroDivisionError as zobj:
        print(zobj)
    print("Division is ",Div)
    print("Sustraction is ",Sub)
        
            
def main():
    
    print("Enter two Number : ")
    
    Value1=int(input())
    Value2=int(input())
    
    Arithmatic(Value1,Value2)

if __name__=="__main__":
    main()