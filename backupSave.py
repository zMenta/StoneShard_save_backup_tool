import os
import shutil
import json

def backupSave():
    with open('config.json') as file:
        data = json.load(file)

    backup_directory = data['save_backup_directory'] + "/exitsave_1"
    exitsave_path = data["stoneShard_save_directory"]
    backup_exist = os.path.isdir(backup_directory)
    exitsave_path_exists = os.path.isdir(exitsave_path)

    print("--START: BACKUP SAVE--")
    # Create directory if backup don't exists #
    if not backup_exist:
        os.mkdir(backup_directory)
        print("--backup path don't exist--")
        print("--backup path created--")
        print("--please try again--")

    else:
        # Remove the backup files #
        if(exitsave_path_exists):
            backup_directory_files = os.listdir(backup_directory)
            if len(os.listdir(exitsave_path)) == 3:
                for file in backup_directory_files:
                    path = os.path.join(backup_directory, file)
                    os.remove(path)
                
                # Copy save files into the backup #
                exitsave_files = os.listdir(exitsave_path)
                for file in exitsave_files:
                    shutil.copy(exitsave_path + "/" + file, backup_directory)
                print("\t--DONE--")
            else:
                print("stoneshard exitsave_1 path folder don't contain all necessary files to backup.")


        else:
            print("--stoneshard exitsave_1 path don't exist--")
