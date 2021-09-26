import discord

from discord.ext import commands


#remember to rewrite it to be able to save pictures and be able to display them so there can be infinite 
#amount of pictures that can be displayed with it, aka sticker bot

class pictures(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def headbob(self, ctx, time: int = -1):
        file_dir = "Pictures/image0.gif"
        file = discord.File(file_dir, filename="Headbob.gif")
        await ctx.message.delete()
        if time == -1:
            await ctx.channel.send(file=file)
            time = "Forever"
        else:
            await ctx.channel.send(file=file, delete_after=time)


def setup(client):
    client.add_cog(pictures(client))
