from pathlib import Path
import json





def create():
    
    config_folder = Path("/etc/celest_bot")
    config_file = Path("/etc/celest_bot/config.json")
    config_data = {}
    
    config_folder.mkdir(exist_ok=True)

    token = str(input(f"Hello, it seems your bot still doesn't have defined token\n"
                      f"please input it here: "))
    
    db_host = str(input(f"Now host server of the database\n"
                      f"please input it here: "))
    
    db_name = str(input(f"Now name of the database\n"
                        f"please input it here: "))
    
    db_user = str(input(f"Now user of the database\n"
                      f"please input it here: "))
    
    db_pass = str(input(f"Now password of the database\n"
                      f"please input it here: "))

    config_data["TOKEN"] = token
    config_data["DB_HOST"] = db_host
    config_data["DB_NAME"] = db_name
    config_data["DB_USER"] = db_user
    config_data["DB_PASS"] = db_pass
    

    with open("/etc/celest_bot/config.json", "w+") as config_file:
        json.dump(config_data, config_file)
