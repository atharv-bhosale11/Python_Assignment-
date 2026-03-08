# Command Line Input

import sys
import os
import time
import schedule
import shutil 
import hashlib
import zipfile

def make_zip(folder):
    timestamp = time.strftime("%Y=%m-%d_%H-%M-%S")
    zip_Name = folder + "_" +timestamp + ".zip"

    #open the zip file 

    zobj = zipfile.ZipFile(zip_Name, "w",zipfile.ZIP_DEFLATED)

    for root,dirs,files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()

def calculate_hash(path):
    hobj = hashlib.md5()
        
    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    fobj.close()

    return hobj.hexdigest()


    
def BackupFiles(Source, Destination):
    Copied_Files = []
    print("Creating the Backup folder for backup process")

    os.makedirs(Destination, exist_ok = True) # If file already exist , there is no error 

    for root, dirs, files in os.walk(Source):
        for file in files :
            src_path = os.path.join(root, file)

            relative =  os.path.relpath(src_path, Source) # convert Absolute path to relative path
            dest_path = os.path.join(Destination,relative)
            os.makedirs(os.path.dirname(dest_path), exist_ok = True) # makedires - >  Nested Folder

            # Copy the files if its new/updated
            if ((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                shutil.copy2(src_path, dest_path)
                Copied_Files.append(relative)

    return Copied_Files 

def marvellousDataShieldStart(Source = "Data"):
    Border  = "-"*50
   
    BackupName = "MarvellousBackup"
    print(Border) 

    print("Backup Process Started Succesfully at : ",time.ctime())
    files = BackupFiles(Source,BackupName)

    zip_files = make_zip(BackupName)
    print(Border) 
    
    print("Backup Completed Succesfully")
    print("Files Copied : ",len(files))

    print("Zip Files gets created : ",zip_files)
    print(Border) 
    

def main():

    Border  = "-"*50
    print(Border)  
    print("----------Marvellous Data Shield System-----------")
    print(Border)

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or  sys.argv[1] == "--H"):
            print("1 : Text autobackup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create and archive of the backup periodically")

        elif (sys.argv[1] == "--u" or  sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval: The time in minutes for periodic Scheduling")
            print("SourceDirectory : NAme of directory to backed up")

        else :
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details ")

    # Python Demo.py 5 Data 
    elif(len(sys.argv) == 3):
        print("Inside project logic")
        print("Time interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])

        # Apply the scheduler

        schedule.every(int(sys.argv[1])).minutes.do(marvellousDataShieldStart, sys.argv[2])

        print(Border) 
    
        print("Data Shield System started succesfully")
        print("Time Interval in minutes :",sys.argv[1])   
        print("Press CTRL + C to stop the execution") 
        
        
        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Invalid number of commad line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details ")


    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__ == "__main__":
    main()
