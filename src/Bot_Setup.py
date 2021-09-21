import discord, json
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)


def sub_cog_loader(Cogs):
    for Cog in Cogs['cogs']:
        CogName = Cog['filename']
        Iscritical = Cog['critical']
        try:
            print(f"Loading {CogName}")
            client.load_extension(f'Cogs.{CogName}')
        except discord.ext.commands.errors.NoEntryPointError:
            print(f"'{CogName}' has no setup function")
        except discord.ext.commands.errors.ExtensionAlreadyLoaded:
            print(f"'{CogName}' is already loaded")
        except discord.ext.commands.errors.ExtensionNotFound:
            if Iscritical:
                raise SystemExit(f'WARNING: Missing critical file "{CogName}"')
            print(f"'{CogName}' couldn't be found")
        except Exception as error:
            if Iscritical:
                raise SystemExit(
                    f'ERROR: Critical file "{CogName}" has met an unexpected error {error}')
            print(f"'{CogName}' met a unexpected error {error}")
        else:
            print("Success")



def cog_loader(Cogs):
    for Cog in Cogs['cogs']:
        CogName = Cog['filename']
        Iscritical = Cog['critical']
        try:
            print(f"Loading {CogName}")
            client.load_extension(f'Cogs.{CogName}')
        except discord.ext.commands.errors.NoEntryPointError:
            print(f"'{CogName}' has no setup function")
        except discord.ext.commands.errors.ExtensionAlreadyLoaded:
            print(f"'{CogName}' is already loaded")
        except discord.ext.commands.errors.ExtensionNotFound:
            if Iscritical:
                raise SystemExit(f'ERROR: Missing critical file "{CogName}"')
            print(f"'{CogName}' couldn't be found")
        except Exception as error:
            if Iscritical:
                raise SystemExit(f'ERROR: Critical file "{CogName}" has met an unexpected error {error}')
            print(f"'{CogName}' met a unexpected error {error}")
        else:
            print("Success")



def Set_up():
    
    try:
        with open("src\Cogs\.Cogs", "r") as coglist:
            coglist = json.load(coglist)
    except FileNotFoundError:
        raise SystemExit("Missing the 'Cogs' manifest File in Cogs folder")
        
    cog_loader(coglist)
        
    print(client.extensions)
    with open("tokens/token.txt", "r") as token:
        token = str(token.read())
    
    client.run(token)




@client.event
async def on_ready():
    print(f"""\n Bot named: {client.user.name}\n
    Started up correctly\n
    ---------------------------------\n
    """)


if __name__ == "__main__":
    Set_up()
