def PrintFactors(No):
    
    for i in range(1,No+1):
        
        if No % i ==0:
            
            print(i,"\t",end="")
            
def main():
    
    print("Enter the Number : ")
    
    Value=int(input())
    
    PrintFactors(Value)

if __name__=="__main__":
    main()