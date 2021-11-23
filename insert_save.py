import os
import os.path as op
import shutil
import json

import backup_save

def insert_save(config):
    backup_directory = config["backup_directory"] + "/exitsave_1"
    backup_directory_exists = op.isdir(backup_directory)

    stoneShard_directory = config["stoneShard_directory"]
    stoneShard_directory_exists = op.isdir(stoneShard_directory)

    print("--START: APPLY SAVE--")
    if not stoneShard_directory_exists:
        os.mkdir(stoneShard_directory)
        print("stoneshard exitsave_1 folder created")
        stoneShard_directory_exists = op.isdir(stoneShard_directory)

    if not backup_directory_exists:
        print("backup folder don't exist")
        pass

    if stoneShard_directory_exists and backup_directory_exists:
        print("copied backup save into Stoneshard")
        backup_files = os.listdir(backup_directory)
        for file in backup_files:
            shutil.copy(backup_directory + "/" + file, stoneShard_directory)
        print("--DONE--")


def main():
    config = backup_save.load_config("config.json")
    insert_save(config)

if __name__ == "__main__":
    main()
