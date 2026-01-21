def Display(No):
   for i in range(No,0,-1):
       print(i,"\t",end="")
        
            
def main():
    
    print("Enter Number : ")
    
    Value=int(input())

    Display(Value)


if __name__=="__main__":
    main()