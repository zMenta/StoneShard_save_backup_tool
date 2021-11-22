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
        data["stoneShard_directory"] = config["stoneShard_directory"]
        data["backup_save_key"] = config["backup_save_key"]
        data["insert_save_key"] = config["insert_save_key"]
        data["exit_key"] = config["exit_key"]
        return data

def backup_save(config):
    backup_directory = config["backup_directory"] + "/exitsave_1"
    backup_directory_exists = op.isdir(backup_directory)

    stoneShard_directory = config["stoneShard_directory"]
    stoneShard_directory_exists = op.isdir(stoneShard_directory)

    print("--START: BACKUP SAVE--")
    if not backup_directory_exists:
        os.mkdir(backup_directory)
        backup_directory_exists = op.isdir(backup_directory)
        print("Created exitsave_1 backup folder")

    if backup_directory_exists:
        # Remove the backup files if Stoneshard_directory is not empty#
        print("Backup exists")
        if(stoneShard_directory_exists and len(os.listdir(stoneShard_directory)) == 3):
            backup_directory_files = os.listdir(backup_directory)
            for file in backup_directory_files:
                path = op.join(backup_directory, file)
                os.remove(path)
            print("REMOVED FILES")
    
        # os.mkdir(backup_directory)
        # print("--backup path don't exist--")
        # print("--backup path created--")
        # print("--please try again--")
    

def main():
    config = load_config("config.json")
    backup_save(config)




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
