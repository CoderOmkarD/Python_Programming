Square=lambda a :a * a

def main():
    Data=[1,2,3,4,5,6,7,8]
    print("Before using Map Function :")
    print(Data)
    MData=list(map(Square,Data))
    print("After using Map Function :")
    print(MData)

if __name__=="__main__":
    main()