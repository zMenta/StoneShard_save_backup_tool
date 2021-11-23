import os
import os.path as op
import shutil

from settings import load_config

def insert_save(config):
    backup_directory = op.join(config["backup_directory"], "exitsave_1")
    backup_directory_exists = op.isdir(backup_directory)

    stone_shard_directory = config["stone_shard_directory"]
    stone_shard_directory_exists = op.isdir(stone_shard_directory)

    print("--START: APPLY SAVE--")
    if not stone_shard_directory_exists:
        os.mkdir(stone_shard_directory)
        print("stoneshard exitsave_1 folder created")
        stone_shard_directory_exists = op.isdir(stone_shard_directory)

    if not backup_directory_exists:
        print("backup folder don't exist")
        pass

    if stone_shard_directory_exists and backup_directory_exists:
        print("copied backup save into Stoneshard")
        backup_files = os.listdir(backup_directory)
        for file in backup_files:
            shutil.copy(backup_directory + "/" + file, stone_shard_directory)
        print("--DONE--")


def main():
    config = load_config("config.json")
    insert_save(config)

if __name__ == "__main__":
    main()
