import discord, json
import cog_loader
from discord.ext import commands
from pathlib import Path

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)



def token_handle():
    
    token_config_folder = Path("/etc/celest_bot")
    token_config_file = Path("/etc/celest_bot/config.json")
    
    if token_config_file.exists():
        with open("/etc/celest_bot/config.json", "r") as config_file:
            config = json.load(config_file)
        return config.get("TOKEN")

    token_config_folder.mkdir(exist_ok=True)
    
    token = str(input(f"Hello, it seems your bot still doesn't have defined token "
                      f"please input it here: "))
    
    token_data = {}
    token_data["TOKEN"] = token

    with open("/etc/celest_bot/config.json", "w+") as config_file:
        json.dump(token_data, config_file)
    return token


def Set_up():
        
    cog_loader.load_cogs(client)
    token = token_handle()
    client.run(token)




@client.event
async def on_ready():
    print(
    f"\n      Bot named: {client.user.name}\n"
    f"        Started up correctly\n"
    f"------------------------------------\n")


if __name__ == "__main__":
    Set_up()
