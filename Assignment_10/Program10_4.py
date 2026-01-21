def PrintEven(no):
    Fact=1
    for i in range(1,no+1):
        if i%2==0:
            print(i,"\t",end="")
   

def main():
    print("Enter the number")
    Value=int(input())
    PrintEven(Value)

    
if __name__=="__main__":
    main()