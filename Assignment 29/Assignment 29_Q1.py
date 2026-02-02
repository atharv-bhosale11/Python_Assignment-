import os

def CheckFile(FileName):
    Ret = os.path.exists(FileName)
    
    if Ret == True:
        print("File Found Successfully!!!!!")
    else:
        print("There is No such File :/")
    return Ret

def main():
    FileName = input("Enter the File Name: ")
    CheckFile(FileName)
    
if __name__=="__main__":
    main()
