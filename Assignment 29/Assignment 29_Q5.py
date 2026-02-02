import sys

def main():
    FileName = sys.argv[1]

    Word = input("Enter the word that you have to check frequency: ")

    fobj = open(FileName,"r")

    data = fobj.read()

    fobj.close()

    Count = 0

    Count = data.count(Word)

    print("Word Found",Count,"times")

if __name__=="__main__":
    main()
