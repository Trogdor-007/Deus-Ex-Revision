#Whenever a new folder is created within the directory "C:\Program Files (x86)\Steam\steamapps\common\Deus Ex\Revision\BiomodSave", then copy the contents of the folder into the directory C:\Program Files (x86)\Steam\steamapps\common\Deus Ex\Revision\BiomodSave\Current.

import os
import shutil
import time

#Change this to be however many seconds you want. 5 seconds will do this 12 times per minute whould should suffice but I would refrain from running it every second.
sleep_time_in_seconds = 5

#Print to command prompt window that scripted has started
print("Script has started")

#The directory where the new folders are created
source_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Deus Ex\\Revision\\BiomodSave"

#The directory where the contents of the new folders will be copied
destination_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Deus Ex\\Revision\\BiomodSave\\Current"

#The list of folders in the source directory
source_dir_list = os.listdir(source_dir)

#Check the timestamps of the source directory creation time and if created within the last 5 seconds, then copy the contents of the folder into the destination directory. Make the for loop below run every 5 seconds.
for i in range(17280):
    print("Script is running through the for loop to copy save games.")
    
    for folder in source_dir_list:        
        if os.path.getctime(os.path.join(source_dir, folder)) > time.time() - sleep_time_in_seconds:
            #Overwrite the contents of the destination directory with the contents of the source directory
            shutil.copytree(os.path.join(source_dir, folder), destination_dir, dirs_exist_ok=True)
    
    #print script is sleeping for 5 seconds
    print(f"Sleeping for {sleep_time_in_seconds} seconds")
    time.sleep(sleep_time_in_seconds)
