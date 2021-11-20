import os
import shutil
import json

print("\033[0;32mSTART\033[0;0;0m")

# Use .txt later for easier use.
#Load CONFIG #
# config_file = open('config.json')
# config = json.load(config_file)

with open('config.json') as file:
    data = json.load(file)

save_backup_directory = data['save_backup_directory'] + "/exitsave_1"
backup_exist = os.path.isdir(save_backup_directory)

# Creates or remove the backup files #
if(backup_exist):
    save_backup_directory_files = os.listdir(save_backup_directory)
    for file in save_backup_directory_files:
        path = os.path.join(save_backup_directory, file)
        os.remove(path)
else:
    os.mkdir(save_backup_directory)

exitsave_path = data["stoneShard_save_directory"]
exitsave_files = os.listdir(exitsave_path)

# Copy save files into the backup #
for file in exitsave_files:
    shutil.copy(exitsave_path + "/" + file, save_backup_directory)


print("\033[0;32mDONE\033[0;0;0m")