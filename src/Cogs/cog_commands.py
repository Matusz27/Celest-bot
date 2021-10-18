from discord.enums import PremiumType
from discord.ext import commands






class Cogs_handle(commands.Cog):
    
    
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def cogs_status(self, ctx):
        self.client.extensions
        await ctx.send("A")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.client.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"{extension} was reloaded", delete_after=8)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx):
        cog_list = [cog for cog in self.client.extensions]
        for cog in cog_list:
            if cog == "Cogs.cog_commands":
                continue
            self.client.reload_extension(f'{cog}')
        await ctx.send("I restarted myself!")
        

def setup(client):
    client.add_cog(Cogs_handle(client))

