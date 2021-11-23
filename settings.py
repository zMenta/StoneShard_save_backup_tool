import os.path as op
import json

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
        