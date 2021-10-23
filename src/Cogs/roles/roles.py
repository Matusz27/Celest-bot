import discord
import emojis
from discord.ext import commands
from database_handle.roles_handle import category_db, role_db





async def emoji_decoder(ctx, raw_emote,guild):
    
    emote = emojis.decode(raw_emote).split(':')[1]
    
    if emojis.count(raw_emote) == 0:
        if not discord.utils.find(lambda e: e.name == emote, guild.emojis):
            await ctx.send(
                "The emote you used is unsuported on this server! \n So it will be ignored")
            return None
    return emote




class roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['role_add'])
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, *, little_payload):
        
        guild = ctx.message.guild
        cut_payload = little_payload.split(';')
        
        if len(cut_payload) < 2:
            await ctx.send("To little arguments, you need to seprate them with ';'")
            return
        
        if len(cut_payload) > 2:
            emote = await emoji_decoder(ctx, cut_payload[2].strip(), guild)
        else:
            emote = None
        
        category_id = category_db.check(cut_payload[1].strip())
        role = cut_payload[0].strip()
        
        if not category_id:
            await ctx.send("Category not found, please try again")
            return
        
        if not discord.utils.find(lambda e: e.name == role, guild.roles):
            await ctx.send("Role not found, please try again")
            return
        
        if role_db.check(role):
            await ctx.send("Role already exists, please try again")
            return
        
        role_db.add(role, emote, category_id[0])
        
        await ctx.send("Success!")

    @commands.command(aliases=['role_del','del_role'])
    @commands.has_permissions(administrator=True)
    async def delete_role(self, ctx, role):
        await ctx.message.delete()

def setup(client):
    client.add_cog(roles(client))
