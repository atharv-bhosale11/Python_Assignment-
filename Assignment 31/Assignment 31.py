import sys
import os

def Display(DirName,Extension):
    if os.path.exists(DirName):
        for file in os.listdir(DirName):
            if file.endswith(Extension):
                print(file)
    else:
        print("Directory does not exist")

def main():
    
    DirName = sys.argv[1]
    Extension = sys.argv[2]
    Display(DirName,Extension)
if __name__=="__main__":
    main()
