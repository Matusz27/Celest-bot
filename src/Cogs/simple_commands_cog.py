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

    @commands.command(aliases=["scre"])
    async def Scree(self, ctx, number=1):
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

    @commands.command(aliases=['rolldice', 'roll', 'diceroll'])
    async def dice(self, ctx, dice_kind=6, dice_number=1):
        msg = f"Celest slowly took {dice_number} of {dice_kind} sided dices into a small cup and with a soft smile started to " \
            f"gently shake it in his claws, before throwing them on a small piece of wood and... \n"
        for dice_nr in range(dice_number):
            result = random.randrange(dice_kind) + 1
            msg += f"Dice nr {dice_nr + 1} Rolled {result} \n"
        await ctx.channel.send(msg)
        
        
def setup(client):
    client.add_cog(Simple_commands(client))

