ChkEven=lambda a : a % 2 == 0

def main():
    Data=[1,2,3,4,5,6,7,8]
    print("Before using filter Function :")
    print(Data)
    MData=list(filter(ChkEven,Data))
    print("After using filter Function :")
    print(MData)

if __name__=="__main__":
    main()