from discord.ext import commands


class polling(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def poll(self, ctx):
        
        await ctx.send()




def setup(client):
    client.add_cog(polling(client))
