import os
import hashlib
import time

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
    start_time = time.time()
    DeleteDuplicateFiles(DirName)
    end_time = time.time()
    print("Duplicate files deleted. Details written to log.txt")
    print("Total Time required for Deleting the Files: ",end_time-start_time)

if __name__ == "__main__":
    main()
