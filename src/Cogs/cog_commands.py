from discord.ext import commands






class Cogs_handle(commands.Cog):
    
    
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.client.load_extension(f'Cogs.{extension}')
        await ctx.send(f"{extension} was loaded", delete_after=8)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"{extension} was unloaded", delete_after=8)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.client.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"{extension} was reloaded", delete_after=8)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def cogs_status(self, ctx):
        self.client.extensions
        await ctx.send("A")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx):
        for cog in self.client.extensions:
            self.client.reload_extension(f'Cogs.{cog}')
        await ctx.send("I restarted myself!", delete_after=8)
        

def setup(client):
    client.add_cog(Cogs_handle(client))

