import sys
def CheckContent(FileName1,FileName2):
    
    fobj1 = open(FileName1,"r")
    fobj2 = open(FileName2,"r")

    data1 = fobj1.read()
    data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if data1==data2:
        print("Success!!!!!")
    else:
        print("Failure :/")

def main():

    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    CheckContent(FileName1,FileName2)

if __name__=="__main__":
    main()
