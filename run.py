from backupSave import backupSave
# import insertSave
import json
import keyboard

with open('config.json') as file:
    data = json.load(file)

backup_key = data["backup_key"]
insert_key = data["insert_save_key"]
exit_key = data["exit_key"]

while True:
    print(keyboard.read_key())
    if keyboard.is_pressed(backup_key):
        backupSave()
    if keyboard.is_pressed(insert_key):
        print("batata")
    if keyboard.is_pressed(exit_key):
        break