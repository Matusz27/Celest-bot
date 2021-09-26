import os
import json
from pathlib import Path

token_config_folder = Path("/etc/celest_bot")
token_config_file = Path("/etc/celest_bot/config.json")

if token_config_file.exists():
    with open("/etc/celest_bot/config.json", "r") as config_file:
        config = json.load(config_file)


class config:
    #SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = "SECRET_KEY"  # config.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #MAIL_USERNAME = config.get("MAIL_USERNAME")
    #MAIL_PASSWORD = config.get("MAIL_PASSWORD")
