from functools import reduce

Max=lambda a,b:max(a,b)

def main():
    
    Data=[1,2,3,4,5,6,7,8,9,10]
  
    print(Data)
    
    Ret=reduce(Max,Data)
    

    print(Ret)

if __name__=="__main__":
    main()