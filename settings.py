import os.path as op
import json

def load_config(config_path):
    print("--[settings]: START --")
    data = dict()

    if not op.exists(config_path):
        print(f"[settings]: Config.json don't exist at {config_path}")
        return data
    
    with open(config_path) as file:
        config = json.load(file)
        data["backup_directory"] = config["backup_directory"]
        data["stone_shard_directory"] = config["stone_shard_directory"]
        data["backup_save_key"] = config["backup_save_key"]
        data["insert_save_key"] = config["insert_save_key"]
        data["exit_key"] = config["exit_key"]
        print("--[settings]: Config loaded | DONE --")
        return data
