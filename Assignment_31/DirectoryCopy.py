import os
import sys
import shutil


def DirectoryCopy(SourceDirName, DestDirName):

    if not os.path.exists(SourceDirName):
        print("There is no such directory present in the folder")
        return

    if os.path.exists(DestDirName):
        print("The FolderName That should newly Created is already exists:")
        print("Please Enter diffrent name of Copy folder")
        return

    shutil.copytree(SourceDirName, DestDirName)

    print(f"Copy Of the Folder/Directory {SourceDirName} is maked Succesessfully")
    print(f"{SourceDirName} ->> {DestDirName}")


def main():

    Border = "-" * 50
    print(Border)
    print("-----Directory Copy System------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Script is used to :")
            print("1 :Make copy of the input folder..")
            print("2 :By using the command line input ..")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as")
            print("ScriptName.py SourceDirectory DestinationDirectory")
            print("SourceDirectory : Name of Directory to Search From")
            print("DestinationDirectory : Name of the Directory you want to copy the data")

        else:
            print("Enable to proceed as there is no such option..")
            print("please use --u or --h for more details...")

    # python Demo.py 5 Data
    elif len(sys.argv) == 3:

        DirectoryCopy(sys.argv[1], sys.argv[2])

    else:
        print("Invalid No.of Command line arguments...")
        print("Enable to proceed as there is no such option..")
        print("please use --u or --h for more details...")

    print(Border)
    print("----------Thank You For Using Our Script----------")
    print(Border)


if __name__ == "__main__":
    main()
