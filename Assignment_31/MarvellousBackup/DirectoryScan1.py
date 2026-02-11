import os


def main():

    DirectoryName = input("Enter the name of the directory : ")

    print("Contents of the directory are :")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("FolderName :", FolderName)

        for SubF in SubFolderName:
            print("SubfolderName:", SubF)

        for fname in FileName:
            print("FileName :", fname)


if __name__ == "__main__":
    main()
