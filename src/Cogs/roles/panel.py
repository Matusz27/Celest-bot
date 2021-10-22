from discord.ext import commands







class Panel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['panel'])
    @commands.has_permissions(administrator=True)
    async def role_panel(self, ctx, option="new"):
        await ctx.message.delete()
        option = option.lower()
        guildid = str(ctx.message.guild.id)
        file_dir_ID = 'Saved files/ID_' + guildid + '.json'
        file_dir_Roles = 'Saved files/Role_' + guildid + '.json'
        if not pathlib.Path(file_dir_ID).exists() and not pathlib.Path(file_dir_Roles).exists():
            msg = 'You need to activate and add at least one role before using me.'
        else:
            if option == 'new':
                msg = await Panel.new(self, file_dir_ID, ctx)
            elif option == 'update':
                msg = await Panel.update(self, file_dir_ID, ctx)
            else:
                msg = "Wrong option, there is only new and update !"
        await ctx.send(msg, delete_after=8)

    async def new(self, file_dir_ID, ctx):
        with open(file_dir_ID, 'r') as json_file:
            messages = json.load(json_file)
        for _, message_value in messages.items():
            try:
                channel = self.client.get_channel(message_value[1])
                message = await channel.fetch_message(message_value[0])
                await message.delete()
            except discord.errors.NotFound:
                continue
        with open(file_dir_ID, 'w') as json_file:
            data = {}
            json.dump(data, json_file)
        await Panel.header(self, file_dir_ID, ctx)
        return('Done')

    async def update(self, file_dir_ID, ctx):
        with open(file_dir_ID, 'r') as json_file:
            messages = json.load(json_file)
        if messages == {} or "":
            return("You have to creat panel before you can update it")
        for _, message_value in messages.items():
            try:
                channel = self.client.get_channel(message_value[1])
                # same as new
                message = await channel.fetch_message(message_value[0])
                await message.delete()
            except discord.errors.NotFound:
                continue
        with open(file_dir_ID, 'w') as json_file:
            data = {}
            json.dump(data, json_file)
        # this only makes it so all the messages are send into the same channel, and not into the message channel
        ctx.channel = channel
        await Panel.header(self, file_dir_ID, ctx)
        return('Done')

    async def header(self, file_dir_ID, ctx):
        message = await ctx.send(content=f"*GryphBot* \n"
                                 f"                           ***Hello There, Friend!~***\n"
                                 f"                *I am here to help you get your roles ^V^\n"
                                 f"                Please, pick some up, from with we have:* \n"
                                 f"")
        json_main.saver(self, file_dir_ID, message)
        await Panel.content(self, ctx, file_dir_ID)

    async def content(self, ctx, file_dir_ID):
        guild = ctx.message.guild
        guild_id = guild.id
        file_dir_category = f"Saved files/Category_{guild_id}.json"
        with open(file_dir_category, 'r') as json_file:
            categories = json.load(json_file)
        for category in categories["Categories"]:
            embed = discord.Embed(colour=discord.Colour(0x460072),
                                  title=f"__***{category}***__")
            with open(f'Saved files/Role_{guild_id}.json', 'r') as json_file:
                roles = json.load(json_file)
            for _, role in roles.items():
                if role[2] == category:
                    embed.add_field(
                        name=f"            *{role[0]}:*", value=f"{role[1]}", inline=True)
            message = await ctx.send(content="", embed=embed)
            json_main.saver(self, file_dir_ID, message)
            await Panel.emotes(self, roles, guild, category, message)

    async def emotes(self, roles, guild, category, message):
        for _, role in roles.items():
            if role[2] == category:
                emote = discord.utils.find(
                    lambda e: e.name == role[1], guild.emojis)
                if emote is None:  # checks if it is standart emote and if it is not checks if it is a server one and makes it avibale for adding
                    emote = emojis.encode(role[1])
                try:
                    await message.add_reaction(emote)
                except discord.errors.HTTPException:
                    logging.error(f"discord.errors.HTTPException")
                    continue
