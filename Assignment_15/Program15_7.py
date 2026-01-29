
GreaterThanFive=lambda a : len(a) > 5

def main():
    
    Data=["Omkar","Hello","India","Pune","Mulshi","Maharashtra","Marvellous","Infosystem"]
  
    print(Data)
    
    Ret=list(filter(GreaterThanFive,Data))
    

    print(Ret)

if __name__=="__main__":
    main()