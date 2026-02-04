import os

def Words(FileName):
    fobj = open(FileName,"r")
    
    Data = fobj.read()
    Words = Data.split()

    print("No. of Words in the Files are: ",len(Words))

    fobj.close()

def main():
    FileName = input("Enter File Name: ")
    Words(FileName)
if __name__=="__main__":
    main()
