import discord, json





def load_cogs(client):

    try:
        with open("src\Cogs\.Cogs", "r") as coglist:
            Cogs = json.load(coglist)
    except FileNotFoundError:
        raise SystemExit("Missing the 'Cogs' manifest File in Cogs folder")

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
                raise SystemExit(
                    f'ERROR: Critical file "{CogName}" has met an unexpected error {error}')
            print(f"'{CogName}' met a unexpected error {error}")
        else:
            print("Success")


def sub_cog_loader(Cogs, client):
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
