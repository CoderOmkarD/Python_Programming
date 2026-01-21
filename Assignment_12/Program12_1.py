def CheckVowel(Value):
    if Value=="a" or Value=='e' or Value=='i' or Value=='o' or Value=='u' or Value=="A" or Value=='E' or Value=='I' or Value=='O' or Value=='U':
        print("It is Vowel")
    else:
        print("It is Consonant")

   

def main():
    
    print("Enter one Char")
    
    Value=str(input())
    
    CheckVowel(Value)

if __name__=="__main__":
    main()