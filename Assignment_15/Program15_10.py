
Even=lambda a : a % 2 == 0 

def main():
    
    Data=[1,2,3,4,5,6,7,8,9,10]
  
    print(Data)
    
    Ret=list(filter(Even,Data))
    
    print("Count of Even Numbers :",len(Ret))

if __name__=="__main__":
    main()