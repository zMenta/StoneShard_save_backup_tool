import os
import shutil
import json


with open('config.json') as file:
    data = json.load(file)

save_backup_directory = data['save_backup_directory'] + "/exitsave_1"
exitsave_path = data["stoneShard_save_directory"]
backup_exist = os.path.isdir(save_backup_directory)
exitsave_path_exists = os.path.isdir(exitsave_path)

def backupSave():
    print("--START--")
    # Creates or remove the backup files #
    if(backup_exist):
        save_backup_directory_files = os.listdir(save_backup_directory)
        for file in save_backup_directory_files:
            path = os.path.join(save_backup_directory, file)
            os.remove(path)
    else:
        os.mkdir(save_backup_directory)


    # Copy save files into the backup #
    if(exitsave_path_exists):
        exitsave_files = os.listdir(exitsave_path)
        for file in exitsave_files:
            shutil.copy(exitsave_path + "/" + file, save_backup_directory)
        print("--DONE--")
    else:
        print("--exitsave_1 path don't exist--")

