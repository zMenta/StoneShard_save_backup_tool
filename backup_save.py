import os
import os.path as op
import json
import shutil

def load_config(config_path):
    data = dict()

    if not op.exists(config_path):
        print("Config file don't exist")
        return data
    
    with open(config_path) as file:
        config = json.load(file)
        data["backup_directory"] = config["backup_directory"]
        data["backup_directory"] = config["backup_directory"]
        data["backup_directory"] = config["backup_directory"]
        data["backup_directory"] = config["backup_directory"]
        return config

config = load_config("config.json")
print(config)

# for key,value in config.items:
#     print(f"{key} = {value}")

# print(config["backup_directory"])


def main():
    pass

if __name__ == "__main__":
    main()

# def backupSave():
#     with open('config.json') as file:
#         data = json.load(file)

#     backup_directory = data['save_backup_directory'] + "/exitsave_1"
#     exitsave_path = data["stoneShard_save_directory"]
#     backup_exist = os.path.isdir(backup_directory)
#     exitsave_path_exists = os.path.isdir(exitsave_path)

#     print("--START: BACKUP SAVE--")
#     # Create directory if backup don't exists #
#     if not backup_exist:
#         os.mkdir(backup_directory)
#         print("--backup path don't exist--")
#         print("--backup path created--")
#         print("--please try again--")

#     else:
#         # Remove the backup files #
#         if(exitsave_path_exists):
#             backup_directory_files = os.listdir(backup_directory)
#             if len(os.listdir(exitsave_path)) == 3:
#                 for file in backup_directory_files:
#                     path = os.path.join(backup_directory, file)
#                     os.remove(path)
                
#                 # Copy save files into the backup #
#                 exitsave_files = os.listdir(exitsave_path)
#                 for file in exitsave_files:
#                     shutil.copy(exitsave_path + "/" + file, backup_directory)
#                 print("\t--DONE--")
#             else:
#                 print("stoneshard exitsave_1 path folder don't contain all necessary files to backup.")


#         else:
#             print("--stoneshard exitsave_1 path don't exist--")
