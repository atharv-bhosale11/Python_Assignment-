import os

def Searching(FileName):
    fobj = open(FileName,"r")
    Data = fobj.read()
    Words = Data.lower().split()

    SearchWord = input("Enter the Word which you have to search: ").lower()
    
    if SearchWord in Words:
        print("Word Found Successfully!!!")
    else:
        print("Word Not Found :/")

    fobj.close()

def main():
    FileName = input("Enter the Name of File: ")
    Searching(FileName)

if __name__=="__main__":
    main()
