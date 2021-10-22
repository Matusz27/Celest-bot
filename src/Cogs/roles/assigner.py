import discord
import emojis
from discord.ext import commands





def get_role_from_emote(emote, guild):

    emote = discord.utils.find(
        lambda e: e.name == emote.name, guild.emojis)

    if not emote:
        emote = emote.name
        emote = emojis.decode(emote)
        
    #database handle

    role_name = discord.utils.get(guild.roles, name="Placeholder")

    if not role_name:
        return None

    return role_name




class Role_assiment(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
              
        guild = self.client.get_guild(payload.guild_id)
        member = payload.member
        emote = payload.emoji
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        
        if member == self.client.user:
            return
        
        #database message check
        
        await message.remove_reaction(emote, member)
        
        role = get_role_from_emote(emote, guild)
        
        if not role:
            msg = "Role that you want optain has been deleted, or the name of it has been changed, or something just went wrong, and if so I am sorry~"
            await channel.send(msg, delete_after=8)
            return
        
        await Role_assiment.assiment(role, member, channel)


    @staticmethod
    async def assiment(role_name, member, channel):
        try:
            if role_name in member.roles:
                await member.remove_roles(role_name)
                await channel.send(f"{member.mention} You not longer have {role_name}!", delete_after = 8)
            else:  
                await member.add_roles(role_name)
                await channel.send(f"{member.mention} You got {role_name}!", delete_after = 8)
        except discord.errors.Forbidden:
            msg = 'Bot has inffsefictient permissons to assign this role. Please talk to the admin'
            await channel.send(msg, delete_after=8)
