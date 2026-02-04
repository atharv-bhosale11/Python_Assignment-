import os

def CopyContent(SrcFile,DesFile):
    SrcFile = open(SrcFile,"r")
    DesFile = open(DesFile,"w")

    Data = SrcFile.read()
    DesFile.write(Data)

    SrcFile.close()
    DesFile.close()

def main():
    SrcFile = input("Enter Source File Name: ")
    DesFile = input("Enter Destination File Name: ")
    print("Copy Content Successfully")
    CopyContent(SrcFile,DesFile)

if __name__=="__main__":
    main()
