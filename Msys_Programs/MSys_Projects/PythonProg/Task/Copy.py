import os
import shutil
import datetime

# set the directory paths for source and destination
source_dir = "D1"
destination_dir = "D2"

# get the current date and time
current_date = datetime.datetime.now()

# create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# iterate over the files in the source directory
for filename in os.listdir(source_dir):
    # get the full path of the file
    file_path = os.path.join(source_dir, filename)

    # get the modification time of the file
    mod_time = os.path.getmtime(file_path)
    mod_date = datetime.datetime.fromtimestamp(mod_time)

    # if the file was modified on the current day, copy it to the destination directory
    if mod_date.date() == current_date.date():
        shutil.copy(file_path, destination_dir)

# delete the source directory
shutil.rmtree(source_dir)

# print a message indicating that the files have been copied and the directory has been deleted
print("Files copied to {} and directory {} deleted".format(destination_dir, source_dir))
