import os
import shutil
import json

# Use .txt later for easier use.
#Load CONFIG #
config_file = open('config.json')
config = json.load(config_file)

this_directory = os.getcwd()
save_backup_directory = os.path.join(this_directory, "exitsave_1") #this_directory + "/exitsave_1"
backup_exist = os.path.isdir(save_backup_directory)

print (save_backup_directory)
print(os.path.join(save_backup_directory, "data.sav"))

# Creates or remove the backup files #
if(backup_exist):
    save_backup_directory_files = os.listdir(save_backup_directory)
    print(save_backup_directory_files)
    for file in save_backup_directory_files:
        path = os.path.join(save_backup_directory, file)
        print(path)
        os.remove(path)
else:
    os.mkdir(save_backup_directory)

exitsave_path = "C:/Users/brent/AppData/Local/StoneShard/characters_v1/character_1/exitsave_1"
exitsave_files = os.listdir(exitsave_path)

# Copy save files into the backup #
for file in exitsave_files:
    shutil.copy("C:/Users/brent/AppData/Local/StoneShard/characters_v1/character_1/exitsave_1/" + file, save_backup_directory)
