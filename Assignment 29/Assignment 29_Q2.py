import os

def main():
    FileName = input("Enter the file name: ")

    fobj = open(FileName,"r")

    Data = fobj.read()

    print("Contents are: ",Data)

    fobj.close()
    
if __name__=="__main__":
    main()
