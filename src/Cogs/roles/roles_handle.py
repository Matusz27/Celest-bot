import discord
import emojis
from discord.ext import commands
from database_handle import roles_handle



class roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['role_add'])
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, role, raw_emote, category):
        
        guild = ctx.message.guild
        emote = emojis.decode(raw_emote).split(':')[1]
        category_id = roles_handle.category.check(category)
        
        if emojis.count(raw_emote) == 0:
            if not discord.utils.find(lambda e: e.name == emote, guild.emojis):
                await ctx.send("The emote you used is unsuported on this server!")
                return
        
        if not category_id:
            await ctx.send("Category not found, please try again")
            return
        
        if not discord.utils.find(lambda e: e.name == role, guild.roles):
            await ctx.send("Role not found, please try again")
            return
        
        if roles_handle.role.check(role):
            await ctx.send("Role already exists, please try again")
            return
        
        roles_handle.role.add(role,emote,category_id[0])
        
        await ctx.send("Success!")
    
    @commands.command()
    async def test(self, ctx, emote):
        print(emojis.decode(emote).split(':'))
        



    @commands.command(aliases=['role_delete'])
    @commands.has_permissions(administrator=True)
    async def delete_role(self, ctx, role):
        await ctx.message.delete()

def setup(client):
    client.add_cog(roles(client))
