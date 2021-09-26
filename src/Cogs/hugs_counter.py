
from discord.ext import commands


class Chizu(commands.Cog):

    def __init__(self, client):
        self.client = client

    #def Add_hug(self, file_dir):
        #with open(file_dir, 'r') as json_file:
            #hugs = json.load(json_file)
            #hugs['hugs'] += 1
        #with open(file_dir, 'w+') as json_file:
            #json.dump(hugs, json_file, indent=2)

    @commands.command(aliases=["Chizu_hug", "Snuggle_Chizu", "Chizu_love"])
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def Hug_chizu(self, ctx):
        file_dir = "Saved files/Chizu_hugs.json"
        #if pathlib.Path(file_dir).exists():
            #Chizu.Add_hug(self, file_dir)
        #else:
            #data = {}
            #data['hugs'] = 1
            #json_main.create(self, file_dir, data)
        #with open(file_dir, 'r') as json_file:
            #hugs = json.load(json_file)
        chizu = self.client.get_user(261669827242885121)
        #msg = f"You hugged {chizu.mention}! She was hugged {hugs['hugs']} times!"
        #await ctx.send(msg)

    @commands.command(aliases=["Chizu_hug_amount"])
    async def Chizus_hugs(self, ctx):
        file_dir = "Saved files/Chizu_hugs.json"
        #if pathlib.Path(file_dir).exists():
            #with open(file_dir, 'r') as json_file:
                #hugs = json.load(json_file)
            #msg = f"Chizu was hugged {hugs['hugs']} times!"
            #await ctx.send(msg)


def setup(client):
    client.add_cog(Chizu(client))
