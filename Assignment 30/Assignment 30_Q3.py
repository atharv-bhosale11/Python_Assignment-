import os

def Line(FileName):
    fobj = open(FileName, "r")
                                  
    for line in fobj:
        words = line.split()
        for word in words:
            print(word)
    fobj.close()

def main():
    FileName = input("Enter File Name: ")
    Line(FileName)

if __name__ == "__main__":
    main()
