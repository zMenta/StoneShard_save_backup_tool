import os
import os.path as op
import shutil

from settings import load_config

def backup_save(config):
    backup_directory = op.join(config["backup_directory"], "exitsave_1")
    backup_directory_exists = op.isdir(backup_directory)

    stone_shard_directory = config["stone_shard_directory"]
    stone_shard_directory_exists = op.isdir(stone_shard_directory)
    stone_shard_number_of_files = len(os.listdir(stone_shard_directory))

    print("--START: BACKUP SAVE--")
    if not backup_directory_exists:
        os.mkdir(backup_directory)
        backup_directory_exists = op.isdir(backup_directory)
        print("Created exitsave_1 backup folder")

    if not stone_shard_directory_exists:
        print("Stone_shard exitsave_1 don't exist")
        return

    if len(os.listdir(stone_shard_directory)) != 3:
        print("stone_shard exitsave_1 folder must have 3 files inside.")
        return

    if backup_directory_exists:
        print("Backup folder exists")
        # Remove the backup files if Stone_shard_directory has 3 files #
        if(stone_shard_directory_exists and stone_shard_number_of_files == 3):
            backup_directory_files = os.listdir(backup_directory)
            for file in backup_directory_files:
                path = op.join(backup_directory, file)
                os.remove(path)
            print("Removed backup files")

            # Copy save files into the backup #
            stone_shard_files = os.listdir(stone_shard_directory)
            for file in stone_shard_files:
                shutil.copy(stone_shard_directory + "/" + file, backup_directory)
            print("Files copied to backup")
            print("--DONE--")


def main():
    config = load_config("config.json")
    backup_save(config)

if __name__ == "__main__":
    main()
