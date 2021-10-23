from discord.ext import commands
from database_handle.roles_handle import category_db, servers_db







class Category(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['category_add', 'cat_add', 'add_cat'])
    @commands.has_permissions(administrator=True)
    async def add_category(self, ctx, category):
        
        try:
            guild_id = ctx.message.guild.id
            guild_local_id = servers_db.check(guild_id)
            
            if not guild_local_id:
                msg = "Roles haven't been activated!"
                await ctx.send(msg)
                return
                
            if category_db.check(category):
                msg = "This category is already created!"
                await ctx.send(msg)
                return
            
            category_db.add(category, guild_local_id)
            
            await ctx.send("Success!")
        except Exception as e:
            print(e)
        

    @commands.command(aliases=['category_del'])
    @commands.has_permissions(administrator=True)
    async def delete_category(self, ctx, category):
        guildid = ctx.message.guild.id
        await ctx.send()


def setup(client):
    client.add_cog(Category(client))
