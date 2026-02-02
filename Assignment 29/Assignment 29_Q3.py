import os

def main():
    SrcFile = open("ABC.txt","r")
    DesFile = open("Demo.txt","w")

    Data = SrcFile.read()
    DesFile.write(Data)

    SrcFile.close()
    DesFile.close()
    
if __name__=="__main__":
    main()
