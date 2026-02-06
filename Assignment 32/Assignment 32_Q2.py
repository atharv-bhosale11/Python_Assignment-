import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while Buffer:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

def FindDuplicateFiles(DirName):
    Result = {}

    for file in os.listdir(DirName):
        filepath = os.path.join(DirName, file)

        if os.path.isfile(filepath):
            checksum = CalculateCheckSum(filepath)

            if checksum in Result:
                Result[checksum].append(file)
            else:
                Result[checksum] = [file]

    log = open("log.txt", "w")

    for checksum in Result:
        if len(Result[checksum]) > 1:
            log.write("Duplicate files:\n")
            for name in Result[checksum]:
                log.write(name + "\n")
            log.write("\n")

    log.close()

def main():
    DirName = input("Enter Directory Name: ")
    FindDuplicateFiles(DirName)
    print("Duplicate file names written into log.txt")

if __name__ == "__main__":
    main()
