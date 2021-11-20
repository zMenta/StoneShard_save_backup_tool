import os
import shutil
import json

print("\033[0;32mSTART\033[0;0;0m")

with open('config.json') as file:
    data = json.load(file)

backup_directory = data['save_backup_directory'] + "/exitsave_1"
exitsave_path = data["stoneShard_save_directory"]
backup_exist = os.path.isdir(backup_directory)
exitsave_exists = os.path.isdir(exitsave_path)

# Creates or remove the stoneshard save files #
if(exitsave_exists):
    stoneshard_save_files= os.listdir(exitsave_path)
    for file in stoneshard_save_files:
        path = os.path.join(exitsave_path, file)
        print(path)
        os.remove(path)
else:
    os.mkdir(exitsave_path)

# Insert backup files #
if(backup_exist):
    backup_files = os.listdir(backup_directory)
    for file in backup_files:
        shutil.copy(backup_directory + "/" + file, exitsave_path)
    print("\033[0;32mDONE\033[0;0;0m")
else:
    print("\033[0;31mbackup don't exist\033[0;0;0m")