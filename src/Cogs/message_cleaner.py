
from discord.ext import commands




class message_cleaner(commands.Cog):

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def Preen(self, ctx, amount=1):
        await ctx.message.delete()
        if amount > 50:
            msg = f"Hey, hey! You trying to preen as many as {amount} feathery messages! You sure about it ? If so, use !yes if no !no"
            await ctx.send(msg, delete_after=20)
        await ctx.channel.purge(limit=amount)
        msg = f"Slowly, celest moved his beak through his long feathers gently cleaning them up, getting out some messages stuck in his feathers, after he was done {amount} of messages was pulled out of his wings"
        await ctx.send(msg, delete_after=20)
        
    @commands.command()
    async def Preen_me(self, ctx, amount=1):
        await ctx.message.delete()
        if amount > 50:
            msg = f"Hey, hey! You trying to preen as many as {amount} feathery messages! You sure about it ? If so, use !yes if no !no"
            await ctx.send(msg, delete_after=20)

        await ctx.channel.purge(limit=amount, check= lambda x: x.author == ctx.author)
        msg = f"Slowly and delicately, celest moved his beak through your hair or feathers, gently cleaning them, getting out some messages that were stuck there, after he was done {amount} of messages was pulled out of them"
        await ctx.send(msg, delete_after=40)


def setup(client):
    client.add_cog(message_cleaner(client))
