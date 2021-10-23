import discord
from discord.ext import commands
from database_handle.roles_handle import servers_db






class active_desactivate(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def activate(self, ctx):
        try:
            guild_id = ctx.message.guild.id
            
            if servers_db.check(guild_id): 
                await ctx.send('Roles cog arealdy activated. If you like to desactivete it use !desactivate')
                return
            
            servers_db.add(guild_id)
            
            await ctx.send("Roles succesfuly activeted. Thank you for choosing GriffBot")
        except Exception as e:
            print (e)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def disactivate(self, ctx, comfirmation = "No"):
        if not comfirmation == "Yes":
            msg = f"""Are you sure ? Roles will be deleted and roles panel will be removed. If you are sure please use !disactivate Yes"""
        else:
            guildid = str(ctx.message.guild.id)
            msg = f"""Roles hadn't been acctivated yet"""
            #try:
                #channel = self.client.get_channel(message_values[1])
                #message = await channel.fetch_message(message_values[0])
                #await message.delete()
            #except discord.errors.NotFound:
                #pass
            msg = 'It is done'
        await ctx.send(msg, delete_after=8)


def setup(client):
    client.add_cog(active_desactivate(client))
