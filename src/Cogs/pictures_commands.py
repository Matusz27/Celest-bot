import discord

from discord.ext import commands


class pictures(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pic(self, ctx, file="headbob"):
        
        
        file = discord.File(filename="Headbob.gif")
        
        await ctx.message.delete()
        await ctx.channel.send(file=file)

    @commands.command()
    async def pic_add(self, ctx, file):

        file = ctx.attachment

        await ctx.message.delete()
        await ctx.channel.send(file=file)



def setup(client):
    client.add_cog(pictures(client))
