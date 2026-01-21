def Table(no):
    print("Table of ",no,"is :")
    for i in range(1,11):
        print(no*i ,"\t", end="")

def main():
    print("Enter the number")
    Value=int(input())
    Table(Value)
    
if __name__=="__main__":
    main()