import discord, imghdr

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

        attachment = ctx.message.attachments[0].read
        if not imghdr.what(attachment):
            ctx.send("The file is not acceptable image")
            return
        
        
        



def setup(client):
    client.add_cog(pictures(client))
