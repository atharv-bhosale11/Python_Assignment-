import os

def Display(DirName,OldExtension,NewExtension):
    if os.path.exists(DirName):
        for file in os.listdir(DirName):
            if file.endswith(OldExtension):
                oldpath = os.path.join(DirName,file)
                NewFile=file.replace(OldExtension,NewExtension)
                newpath = os.path.join(DirName,NewFile)
                os.rename(oldpath,newpath)
                print(file,"rename to", NewFile)
            
    else:
        print("Directory does not exist")

    
def main():

    DirName =  input("Enter Directory Name: ")
    OldExtension = input("Enter old Extension: ")
    NewExtension = input("Enter New Extension: ")
    Display(DirName,OldExtension,NewExtension)
if __name__=="__main__":
    main()
