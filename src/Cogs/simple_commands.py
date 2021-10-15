import random

from discord.ext import commands



class Simple_commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        ping = round(self.client.latency * 1000)
        msg = f"Hello there! I work as intended with ping of {ping}ms. I hope you will have a nice day ^v^"
        await ctx.send(msg)

    @commands.command(aliases=["scree"])
    async def Scre(self, ctx, number=1):
        characters = ['Scre']
        for _ in range(number):
            characters.append('e')
        characters.append("!")
        msg = "".join(characters)
        await ctx.send(msg)
        
    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def Chirp(self, ctx, amount=1):
        if amount > 100:
            amount = 100
        msg = " ".join(["Chirp!" for _ in range(amount)])
        await ctx.send(msg)
        
    @commands.command()
    async def Rax_stream(self, ctx):
        await ctx.send("https://picarto.tv/Disregard67")


        
        
def setup(client):
    client.add_cog(Simple_commands(client))

