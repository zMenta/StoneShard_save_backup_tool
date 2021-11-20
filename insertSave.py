import os
import shutil
import json

with open('config.json') as file:
    data = json.load(file)

save_backup_directory = data['save_backup_directory'] + "/exitsave_1"
exitsave_path = data["stoneShard_save_directory"]
backup_exist = os.path.isdir(save_backup_directory)
exitsave_exists = os.path.isdir(exitsave_path)

# Creates or remove the stoneshard files #
if(exitsave_exists):
    stoneshard_save_files= os.listdir(exitsave_path)
    for file in stoneshard_save_files:
        path = os.path.join(exitsave_path, file)
        print(path)
        os.remove(path)
else:
    os.mkdir(exitsave_path)