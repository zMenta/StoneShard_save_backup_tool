import os
import os.path as op
import shutil

from settings import load_config


def backup_save(config):
    backup_directory = op.join(config["backup_directory"])
    backup_directory_exists = op.isdir(backup_directory)

    stoneshard_directory = config["stoneshard_directory"]
    stoneshard_directory_exists = op.isdir(stoneshard_directory)

    print("----------- [Backup_Save]: W O R K I N G ----------")
    print("---------------------------------------------------\n")
    if not backup_directory_exists:
        os.mkdir(backup_directory)
        backup_directory_exists = op.isdir(backup_directory)
        print(f"-- [Backup_Save]: Creating A Backup Folder In \n\n{backup_directory}")
        print("---------------------------------------------------")

    if not stoneshard_directory_exists:
        print(
            f"-- [Backup_Save]: The Stoneshard Directory\n\n{stoneshard_directory}\n\nDoesn't Exist --"
        )
        print("---------------------------------------------------")
        return

    if len(os.listdir(stoneshard_directory)) != 3:
        print(
            f"-- [Backup_Save]: The Folder\n\n{stoneshard_directory}\n\nMust Have 3 Files Inside It --"
        )
        print("---------------------------------------------------")
        return

    if backup_directory_exists:
        stone_shard_number_of_files = len(os.listdir(stoneshard_directory))
        if stoneshard_directory_exists and stone_shard_number_of_files == 3:
            backup_directory_files = os.listdir(backup_directory)
            for file in backup_directory_files:
                path = op.join(backup_directory, file)
                os.remove(path)
            print(f"-- [Backup_Save]: Removed The Backup Files In:\n\n{backup_directory}\n")
            print("---------------------- And Then -------------------\n")
            stone_shard_files = os.listdir(stoneshard_directory)
            for file in stone_shard_files:
                shutil.copy(stoneshard_directory + "/" + file, backup_directory)
            print(
                f"-- [Backup_Save]: Copied Files From:\n\n{stoneshard_directory}\n\n----------------------- To ------------------------\n\n{backup_directory}\n"
            )
            print("---------------------------------------------------")
            print("----------- [Backup_Save]: F I N I S H E D --------")
            print("---------------------------------------------------")


def main():
    config = load_config("config.py")
    backup_save(config)


if __name__ == "__main__":
    main()
