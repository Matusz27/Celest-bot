import database_handle
from discord.ext import commands


class hugs_handle(commands.Cog):

    def __init__(self, client):
        self.client = client


    @staticmethod
    async def rejection(ctx):
        recipiants = database_handle.fetch_hug_recipants()
        msg = "You need to specify who you wanna hug! \nYou can hug:\n"
        for number, recipiant in enumerate(recipiants):
            msg += f"{number + 1}.  {recipiant['name'].capitalize()}\n"
        await ctx.send(msg)
        hugs_handle.hug.reset_cooldown(ctx)


    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def hug(self, ctx, person = None):
        
        if person is None:
            await hugs_handle.rejection(ctx)
            return
        
        person = person.lower()
        
        if not database_handle.check_for_hug_recipiant(person):
            await hugs_handle.rejection(ctx)
            return
    
        database_handle.increment_hug(person)
        
        hugs_after_addition = database_handle.fetch_hugs(person)
        
        msg = f"You hugged {person.capitalize()}! They were hugged {hugs_after_addition[0]} times!"
        await ctx.send(msg)

    @commands.command(aliases=["Chizu_hug_amount"])
    async def hugs(self, ctx, person=None):
        
        if person is None:
            hugs = database_handle.fetch_hugs()
            msg = "Pepole that were hugged and can be hugged!\n"
            for person in hugs:
                msg += f"{person['name'].capitalize()} was hugged {person['amount']} times!\n"
        else:
            if not database_handle.check_for_hug_recipiant(person):
                ctx.send("They aren't huggable yet! Or you spelled it wrong cutie~")
                return
            hugs = database_handle.fetch_hugs(person)
            msg = f"{person.capitalize()} was hugged {hugs[0]['amount']} times!"
        
        await ctx.send(msg)


def setup(client):
    client.add_cog(hugs_handle(client))
