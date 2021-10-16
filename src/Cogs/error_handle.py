
from discord.ext import commands




class Error(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You're not permited to do use {ctx.command} cuz you are not permited to {error}, sorry", delete_after=8)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("You're trying to use not existing command, check your spelling cutie", delete_after=8)
        elif isinstance(error, commands.CommandOnCooldown):
            Cooldown = error.retry_after
            await ctx.send(f"You're using this command too much! You need to wait {Cooldown:.2f}s!", delete_after=8)



def setup(client):
    client.add_cog(Error(client))
