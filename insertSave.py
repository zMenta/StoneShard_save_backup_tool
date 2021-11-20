import os
import shutil
import json

def insertSave():

    with open('config.json') as file:
        data = json.load(file)

    backup_directory = data['save_backup_directory'] + "/exitsave_1"
    exitsave_path = data["stoneShard_save_directory"]
    backup_exist = os.path.isdir(backup_directory)
    exitsave_exists = os.path.isdir(exitsave_path)
    
    print("--START: APPLY SAVE--")
    # Remove the stoneshard save file if the file exists#
    if(exitsave_exists):
        stoneshard_save_files= os.listdir(exitsave_path)
        for file in stoneshard_save_files:
            path = os.path.join(exitsave_path, file)
            os.remove(path)
        os.rmdir(exitsave_path)

    def insertFiles():
        os.mkdir(exitsave_path)
        backup_files = os.listdir(backup_directory)
        for file in backup_files:
            shutil.copy(backup_directory + "/" + file, exitsave_path + "/exitsave_1")
        print("\t--DONE--")

    # Insert backup files #
    backup_files = os.listdir(backup_directory)
    print(backup_exist)
    if(backup_exist and len(backup_files) != 0):
        if exitsave_exists:
            os.rmdir(exitsave_path)
            insertFiles()
        else:
            insertFiles()
    else:
        print("--backup don't exist--")