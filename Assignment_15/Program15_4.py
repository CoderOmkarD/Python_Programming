from functools import reduce

Add=lambda a,b:a+b 

def main():
    
    Data=[1,2,3,4,5,6,7,8,9,10]
  
    print(Data)
    
    Ret=reduce(Add,Data)
    

    print(Ret)

if __name__=="__main__":
    main()