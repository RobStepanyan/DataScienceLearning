import os
import time
import zipfile

# Sources of files, that are going to be archived
sources = ["file1.txt", "file2.txt", "pic.bmp"]

# The name of archive that will be made
backup_name = time.strftime("%Y-%m-%d %H,%M,%S") + ".zip"

# Target directory for keeping backups
target = time.strftime("%Y-%m-%d")
if not os.path.exists(target):
    os.mkdir(target)

# Creating the backup
with zipfile.ZipFile(target+os.sep+backup_name, "w") as myzip:
    for source in sources:
        myzip.write(source)
        print(source, "is archived successfully!")
    print("Backup is completed!!")
