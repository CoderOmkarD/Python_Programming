def GetBinary(No):
    binary_value=bin(No)[2:]
    print("Binary Representation is :",binary_value)

def main():
    print("Enter the number :")
    Value=int(input())
    GetBinary(Value)
    

if __name__=="__main__":
    main()