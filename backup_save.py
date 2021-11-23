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

    print("--[backup_save]: START--")
    if not backup_directory_exists:
        os.mkdir(backup_directory)
        backup_directory_exists = op.isdir(backup_directory)
        print(f"[backup_save]: create backup folder at {backup_directory}")

    if not stone_shard_directory_exists:
        print(f"[backup_save]: StoneShard exitsave_1 don't exist at {stone_shard_directory}")
        return

    if len(os.listdir(stone_shard_directory)) != 3:
        print(f"[backup_save]: StoneShard folder at {stone_shard_directory} must have 3 files inside")
        return

    if backup_directory_exists:
        # Remove the backup files if Stone_shard_directory has 3 files #
        if(stone_shard_directory_exists and stone_shard_number_of_files == 3):
            backup_directory_files = os.listdir(backup_directory)
            for file in backup_directory_files:
                path = op.join(backup_directory, file)
                os.remove(path)
            print(f"[backup_save]: Removed backup files at {backup_directory}")

            # Copy save files into the backup #
            stone_shard_files = os.listdir(stone_shard_directory)
            for file in stone_shard_files:
                shutil.copy(stone_shard_directory + "/" + file, backup_directory)
            print(f"[backup_save]: Copied files from Stoneshard {stone_shard_directory} to Backup {backup_directory}")
            print("--[backup_save]: DONE--")


def main():
    config = load_config("config.json")
    backup_save(config)

if __name__ == "__main__":
    main()
