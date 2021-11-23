import os
import os.path as op
import shutil

from settings import load_config

def backup_save(config):
    backup_directory = config["backup_directory"] + "/exitsave_1"
    backup_directory_exists = op.isdir(backup_directory)

    stoneShard_directory = config["stoneShard_directory"]
    stoneShard_directory_exists = op.isdir(stoneShard_directory)
    stoneShard_number_of_files = len(os.listdir(stoneShard_directory))

    print("--START: BACKUP SAVE--")
    if not backup_directory_exists:
        os.mkdir(backup_directory)
        backup_directory_exists = op.isdir(backup_directory)
        print("Created exitsave_1 backup folder")

    if not stoneShard_directory_exists:
        print("Stoneshard exitsave_1 don't exist")

    if len(os.listdir(stoneShard_directory)) != 3:
        print("stoneshard exitsave_1 folder must have 3 files inside.")

    if backup_directory_exists:
        print("Backup folder exists")
        # Remove the backup files if Stoneshard_directory has 3 files #
        if(stoneShard_directory_exists and stoneShard_number_of_files == 3):
            backup_directory_files = os.listdir(backup_directory)
            for file in backup_directory_files:
                path = op.join(backup_directory, file)
                os.remove(path)
            print("Removed backup files")

            # Copy save files into the backup #
            stoneShard_files = os.listdir(stoneShard_directory)
            for file in stoneShard_files:
                shutil.copy(stoneShard_directory + "/" + file, backup_directory)
            print("Files copied to backup")
            print("--DONE--")


def main():
    config = load_config("config.json")
    backup_save(config)

if __name__ == "__main__":
    main()
