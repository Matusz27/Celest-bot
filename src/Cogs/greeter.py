
from discord.ext import commands






class goodbyer_and_greeter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild.id
        if guild == 441772481481670656:
            Rules1 = self.client.get_channel(491690394069893120)
            Rules2 = self.client.get_channel(608836659206684713)
            Roles = self.client.get_channel(650243960274550805)
            World = self.client.get_channel(623919121439916050)
            guild = (member.guild)
            msg = f"Welcome {member.mention}! With you, there are now {guild.member_count} members. Please go over to {Rules1.mention}, and read them! There is a password in here. You don't need to read the {Rules2.mention}, though! \n \n" \
                f"Once that's all done and good, and you've said the password, go over to {Roles.mention}! And request some roles! We have alot for you to chose from! Also maybe look into{World.mention} there is a map and everthing~"
            channel = self.client.get_channel(472078798251360266)
            await channel.send(msg)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild.id
        if guild == 441772481481670656:
            guild = (member.guild)
            msg = f"Aw... {member.nick} left! Without them, there are now {guild.member_count} members. \n" \
                f"Hopefuly they will be back soon!"
            channel = self.client.get_channel(472078798251360266)
            await channel.send(msg)


def setup(client):
    client.add_cog(goodbyer_and_greeter(client))
