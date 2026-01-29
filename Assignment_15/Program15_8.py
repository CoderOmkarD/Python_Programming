
ChkDivisible=lambda a : a % 5 ==  0 and a % 3 == 0

def main():
    
    Data=[11,2,345,663,45,45,46,23,76,678,67,98]
  
    print(Data)
    
    Ret=list(filter(ChkDivisible,Data))
    

    print(Ret)

if __name__=="__main__":
    main()