def DisplayGrade(No):
    
    if No> 100:
        print("Marks should be in Between 0 to 100")
        return
    
    
    if No>=75:
        print("Distinction")
    elif No >= 60 and No <=74:
        print("First Class")
    elif No>=50 and No<=59:
        print("Second Class")
    elif No < 50:
        print("Fail")
        

def main():
    
    Value=0
    print("Enter the Marks :")
    Value=int(input())
    

    DisplayGrade(Value)
    

if __name__=="__main__":
    main()