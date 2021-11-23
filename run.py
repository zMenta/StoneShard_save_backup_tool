import keyboard

from settings import load_config
from backup_save import backup_save
from insert_save import insert_save

def main():
    config = load_config("config.json")

    backup_key = config["backup_save_key"]
    insert_key = config["insert_save_key"]
    exit_key = config["exit_key"]

    while True:
        keyboard.read_key()
        if keyboard.is_pressed(backup_key):
            backup_save(config)
        if keyboard.is_pressed(insert_key):
            insert_save(config)
        if keyboard.is_pressed(exit_key):
            break

if __name__ == "__main__":
    main()
