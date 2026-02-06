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

def DeleteDuplicateFiles(DirName):
    Result = {}

    for file in os.listdir(DirName):
        filepath = os.path.join(DirName, file)

        if os.path.isfile(filepath):
            checksum = CalculateCheckSum(filepath)

            if checksum in Result:
                Result[checksum].append(filepath)
            else:
                Result[checksum] = [filepath]

    log = open("log.txt", "w")

    for checksum in Result:
        files = Result[checksum]

        if len(files) > 1:
            for dup_file in files[1:]:
                os.remove(dup_file)
                log.write("Deleted: " + dup_file + "\n")
    log.close()

def main():
    DirName = input("Enter Directory Name: ")
    DeleteDuplicateFiles(DirName)
    print("Duplicate files deleted. Details written to log.txt")

if __name__ == "__main__":
    main()
