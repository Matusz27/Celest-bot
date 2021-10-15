import discord, json
import cog_loader, config
from discord.ext import commands
from pathlib import Path

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)



def Set_up():
    cog_loader.load_cogs(client)
    client.run(config.TOKEN)


@client.event
async def on_ready():
    print(
    f"\n      Bot named: {client.user.name}\n"
    f"        Started up correctly\n"
    f"------------------------------------\n")


if __name__ == "__main__":
    Set_up()
