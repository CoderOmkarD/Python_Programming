import os


def main():

    print("Enter the FileName")
    FileName = input()

    print("Enter the WORD to check..")
    Key = input()
    if not (os.path.exists(FileName)):
        print("There is no such file in the directory...")
        return -1

    fobj = open(FileName, "r")

    Data = fobj.read()

    words = Data.split()

    flag = False

    for word in words:
        if word == Key:
            flag = True
            break

    if flag:
        print(f"{Key} is found in the {FileName}")
    else:
        print(f"{Key} not found in {FileName}")

    print(" Hehe ")
if __name__ == "__main__":
    main()
