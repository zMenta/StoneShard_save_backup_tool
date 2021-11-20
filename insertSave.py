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
    # verifies if stoneshard exit_save exists#
    if not exitsave_exists:
        os.mkdir(exitsave_path)
        print("--stoneshard exitsave_1 path don't exist--")
        print("--stoneshard exitsave_1 created--")
        print("--please try again--")

    else:
        # Insert files from backup #
        backup_files = os.listdir(backup_directory)
        for file in backup_files:
            print(file)
            shutil.copy(backup_directory + "/" + file, exitsave_path)
        print("\t--DONE--")
