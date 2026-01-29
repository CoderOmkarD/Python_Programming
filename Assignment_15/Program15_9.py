from functools import reduce

Mult=lambda a , b : a*b

def main():
    
    Data=[1,2,3,4,5,6,7,8,9,10]
  
    print(Data)
    
    Ret=reduce(Mult,Data)
    
    print(Ret)

if __name__=="__main__":
    main()