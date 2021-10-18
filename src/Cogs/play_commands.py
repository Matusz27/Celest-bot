import random

from discord.ext import commands


class games(commands.Cog):
    
    
    @commands.command(aliases=['rolldice', 'roll', 'diceroll'])
    async def dice(self, ctx, dice_kind=6, dice_number=1):
        msg = f"Celest slowly took {dice_number} of {dice_kind} sided dices into a small cup and with a smile started to " \
            f"gently shake it in his claws, before throwing the dice onto small wooden table and... \n"
        for dice_nr in range(dice_number):
            result = random.randrange(dice_kind) + 1
            msg += f"Dice nr {dice_nr + 1} Rolled {result} \n"
        await ctx.channel.send(msg)


def setup(client):
    client.add_cog(games(client))
