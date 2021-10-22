from discord.ext import commands
from database_handle import roles_handle







class Category(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['category_add'])
    @commands.has_permissions(administrator=True)
    async def Add_category(self, ctx, category):
        
        guild_id = ctx.message.guild.id
        guild_local_id = roles_handle.role_servers.check_server(guild_id)
        
        if not guild_local_id:
            msg = "Roles haven't been activated!"
            await ctx.send(msg)
            return
            
        if roles_handle.category.check(category):
            msg = "This category is already created!"
            await ctx.send(msg)
            return
        
        roles_handle.category.add(category)
        
        await ctx.send("Success!")
        

    @commands.command(aliases=['category_del'])
    @commands.has_permissions(administrator=True)
    async def delete_category(self, ctx, category):
        guildid = ctx.message.guild.id
        await ctx.send()


def setup(client):
    client.add_cog(Category(client))
