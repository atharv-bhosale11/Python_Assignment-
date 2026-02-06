import os
import shutil

def Copy(SrcDir,DesDir):
    if os.path.exists(SrcDir):
        if not os.path.exists(DesDir):
            os.mkdir(DesDir)
        for file in os.listdir(SrcDir):
            SrcPath = os.path.join(SrcDir,file)
            if os.path.isfile(SrcPath):
                despath = os.path.join(DesDir,file)
                shutil.copy(SrcPath,despath)
                print("File Succesfully copied!!!!!!")
    else:
        print("Directory Not exist :/")
        


def main():
    SrcDir = input("Enter Source Directory: ")
    DesDir= input("Enter Desination Directory: ")
    Copy(SrcDir,DesDir)


if __name__=="__main__":
    main()
