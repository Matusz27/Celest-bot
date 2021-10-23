from discord.ext import commands







class Panel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def new_panel(self, ctx):
        guildid = ctx.message.guild.id
        
        await ctx.send()

    async def new(self, ctx):
        await Panel.header(self, ctx)


    async def header(self, ctx):
        message = await ctx.send(
        content=f"*GryphBot* \n"
f"                           ***Hello There, Friend!~***\n"
f"                *I am here to help you get your roles ^V^\n"
f"                Please, pick some up, from with we have:* \n"
f"")
