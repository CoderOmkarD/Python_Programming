import os


def DirectoryScanner(DirectoryName):

    print("Contents of the directory are :")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("FolderName :", FolderName)

        for SubF in SubFolderName:
            print("SubfolderName:", SubF)

        for fname in FileName:
            print("FileName :", fname)


def main():

    DirectoryName = input("Enter the name of the directory : ")

    if os.path.exists(DirectoryName):
        DirectoryScanner(DirectoryName)
    else:
        print("There is no such Directory")


if __name__ == "__main__":
    main()
