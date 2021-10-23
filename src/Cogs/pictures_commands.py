import imghdr,discord
from database_handle import pictures as pictures_db
from io import BytesIO
from discord.ext import commands


class pictures(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pic(self, ctx, name=None):
        
        if not name:
            names = pictures_db.fetch_all_names()
            msg = "Current pictures:\n"
            for number, name in enumerate(names):
                msg += f"{number + 1}.  {name[0]}\n"
            await ctx.send(msg)
            return
                
        if not pictures_db.check_for_picture(name):
            await ctx.send("There is no such a picture!")
            return
        
        bytes = pictures_db.fetch(name)[0].tobytes()
        pic = discord.File(BytesIO(bytes),filename=f"{name}.{imghdr.what(None, bytes)}")
            
        await ctx.message.delete()
        await ctx.channel.send(file=pic)


    @commands.command(aliases=["add_pic"])
    async def pic_add(self, ctx, name):
        
        if not ctx.message.attachments:
            await ctx.send("There is no file!")
            return
        
        attachment_bytes = await ctx.message.attachments[0].read()
        
        if not imghdr.what(None, attachment_bytes):
            await ctx.send("The file is not acceptable image format!")
            return
        
        if pictures_db.check_for_picture(name):
            await ctx.send("This name is already in use!")
            return
        
        pictures_db.add(attachment_bytes, name)
        
        await ctx.send("Picture has been added!")
        

def setup(client):
    client.add_cog(pictures(client))
