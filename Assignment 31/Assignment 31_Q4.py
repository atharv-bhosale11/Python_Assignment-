import os
import shutil

def CopyFiles(SourceDir, DestDir, Extension):
    if os.path.exists(SourceDir):

        if not os.path.exists(DestDir):
            os.mkdir(DestDir)

        for file in os.listdir(SourceDir):
            if file.endswith(Extension):
                source_path = os.path.join(SourceDir, file)
                dest_path = os.path.join(DestDir, file)

                shutil.copy(source_path, dest_path)
                print(file, "copied successfully")

    else:
        print("Source directory does not exist")

def main():
    SourceDir = input("Enter Source Directory Name: ")
    DestDir = input("Enter Destination Directory Name: ")
    Extension = input("Enter File Extension: ")

    CopyFiles(SourceDir, DestDir, Extension)

if __name__ == "__main__":
    main()
