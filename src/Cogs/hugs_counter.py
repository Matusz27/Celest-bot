import database_handle
from discord.ext import commands


class hugs_handle(commands.Cog):

    def __init__(self, client):
        self.client = client


    @staticmethod
    async def rejection(ctx, msg):
        recipiants = database_handle.fetch_hug_recipants()
        msg += "\nYou can hug:\n"
        for number, recipiant in enumerate(recipiants):
            msg += f"{number + 1}.  {recipiant['name'].capitalize()}\n"
        await ctx.send(msg)
        ctx.command.reset_cooldown(ctx)


    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def hug(self, ctx, person = None):
        
        if person is None:
            await hugs_handle.rejection(ctx,"You hugged yourself!")
            return
        
        person = person.lower()
        
        if not database_handle.check_for_hug_recipiant(person):
            await hugs_handle.rejection(ctx, "I didn't found who you're looking for")
            return
    
        database_handle.increment_hug(person)
        
        hugs_after_addition = database_handle.fetch_hugs(person)
        
        msg = f"You hugged {person.capitalize()}! They were hugged {hugs_after_addition[0]} times!"
        await ctx.send(msg)

    @commands.command(aliases=["Chizu_hug_amount"])
    async def hugs(self, ctx, person=None):
        
        if person is None:
            hugs = database_handle.fetch_hugs()
            msg = "Pepole that were hugged and can be hugged!\n\n"
            hugs_sorted = sorted(hugs, key=lambda d: d['amount'], reverse=True)
            for person in hugs_sorted:
                msg += f"{person['name'].capitalize()} was hugged {person['amount']} times!\n"
        else:
            if not database_handle.check_for_hug_recipiant(person):
                ctx.send("They aren't huggable yet! Or you spelled it wrong cutie~")
                return
            hugs = database_handle.fetch_hugs(person)
            msg = f"{person.capitalize()} was hugged {hugs[0]['amount']} times!"
        
        await ctx.send(msg)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_hugs(self, ctx, person=None):
        
        if person is None:
            await ctx.send("You need to specify who you wanna add")
            return

        person = person.lower()

        if database_handle.check_for_hug_recipiant(person):
            await ctx.send("They are already signed up for snuggling!")
            return

        database_handle.add_hug_recipiant(person)

        msg = f"You added {person.capitalize()}! They are now huggable!"
        await ctx.send(msg)
        



def setup(client):
    client.add_cog(hugs_handle(client))
