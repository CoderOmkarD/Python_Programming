import os


def main():

    print("Enter the FileName")
    FileName = input()

    if not (os.path.exists(FileName)):
        print("There is no such file in the directory...")
        return -1

    fobj = open(FileName, "r")

    for lines in fobj:
        print(lines)


if __name__ == "__main__":
    main()
