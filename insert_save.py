import os
import os.path as op
import shutil

from settings import load_config

def insert_save(config):
    backup_directory = op.join(config["backup_directory"], "exitsave_1")
    backup_directory_exists = op.isdir(backup_directory)

    stone_shard_directory = config["stone_shard_directory"]
    stone_shard_directory_exists = op.isdir(stone_shard_directory)

    print("--[insert_save]: START --")
    if not stone_shard_directory_exists:
        os.mkdir(stone_shard_directory)
        print(f"[insert_save]: Stoneshard exitsave_1 folder created at {stone_shard_directory}")
        stone_shard_directory_exists = op.isdir(stone_shard_directory)

    if not backup_directory_exists:
        print(f"[insert_save]: Backup folder don't exist at {backup_directory}")
        pass

    if stone_shard_directory_exists and backup_directory_exists:
        print(f"[insert_save]: Copied backup save from {backup_directory} to Stoneshard {stone_shard_directory}")
        backup_files = os.listdir(backup_directory)
        for file in backup_files:
            shutil.copy(backup_directory + "/" + file, stone_shard_directory)
        print("--[insert_save]: DONE --")


def main():
    config = load_config("config.json")
    insert_save(config)

if __name__ == "__main__":
    main()
