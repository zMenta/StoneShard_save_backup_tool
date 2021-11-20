import os
import shutil
import json

# Use .txt later for easier use.
config_file = open('config.json')
config = json.load(config_file)
print(config)

local_directory = os.getcwd()
# print(local_directory)


# os.rmdir(local_directory + "/folder") #remove directory / remove folder


# shutil.copy("C:/Users/brent/AppData/Local/StoneShard/characters_v1/character_1/exitsave_1/save.map", local_directory)
save_backup_directory = local_directory + "/exitsave_1"
os.mkdir(save_backup_directory)

exitsave_path = "C:/Users/brent/AppData/Local/StoneShard/characters_v1/character_1/exitsave_1"

exitsave_files = os.listdir(exitsave_path)
print(exitsave_files)

for file in exitsave_files:
    shutil.copy("C:/Users/brent/AppData/Local/StoneShard/characters_v1/character_1/exitsave_1/" + file, save_backup_directory)
