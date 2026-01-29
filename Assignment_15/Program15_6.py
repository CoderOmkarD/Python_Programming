from functools import reduce

Min=lambda a,b:min(a,b)

def main():
    
    Data=[1,2,3,4,5,6,7,8,9,10]
  
    print(Data)
    
    Ret=reduce(Min,Data)
    

    print(Ret)

if __name__=="__main__":
    main()