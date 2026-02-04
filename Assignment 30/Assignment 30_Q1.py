import os

def Lines(FileName):
    fobj = open(FileName,"r")
    
    Data = fobj.readlines()
    Count = len(Data)

    fobj.close()

    print("No. of Lines in the Files are: ",Count)

def main():
    FileName = input("Enter File Name: ")
    Lines(FileName)
if __name__=="__main__":
    main()
