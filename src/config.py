import json
import config_creator
from pathlib import Path

token_config_folder = Path("/etc/celest_bot")
token_config_file = Path("/etc/celest_bot/config.json")

if not token_config_file.exists():
    config_creator.create()


with open("/etc/celest_bot/config.json", "r") as config_file:
    config_data = json.load(config_file)


class config:
    TOKEN   = config_data.get("TOKEN")
    DB_HOST = config_data.get("DB_HOST")
    DB_NAME = config_data.get("DB_NAME")
    DB_USER = config_data.get("DB_USER")
    DB_PASS = config_data.get("DB_PASS")
