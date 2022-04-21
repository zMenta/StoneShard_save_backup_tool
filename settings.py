def load_config(config_path):
    print("------- StoneShard Exit Save Backup Tool ----------")
    print("---------------------------------------------------")
    print("----------- [Settings]: L O A D I N G -------------")
    print("---------------------------------------------------")
    print("---- 1. Select 'Save And Exit' In The Game --------")
    print("---- 2. Then Press [F5] To Backup The Exit Save ---")
    print("---------------------------------------------------")
    print("------- To Load The Exit Save, Press [F8] ---------")
    print("------- To Exit The Program, Press [F9] -----------")
    print("---------------------------------------------------")
    data = dict()

    with open(config_path) as file:
        config = json.load(file)

        data["backup_directory"] = (
            "%s\\StoneShard\\characters_v1\\character_1\\.exitsave_1\\"
            % os.environ["LOCALAPPDATA"]
        )
        if not os.path.exists(data["backup_directory"]):
            os.makedirs(data["backup_directory"])

        data["stoneshard_directory"] = (
            "%s\\StoneShard\\characters_v1\\character_1\\exitsave_1\\"
            % os.environ["LOCALAPPDATA"]
        )
        if not os.path.exists(data["stoneshard_directory"]):
            os.makedirs(data["stoneshard_directory"])

        data["backup_save_key"] = config["backup_save_key"]
        data["insert_save_key"] = config["insert_save_key"]
        data["exit_key"] = config["exit_key"]
        return data
