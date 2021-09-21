import socket, urllib.request
from discord.ext import commands


class Server_commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def server(self, ctx):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        location = ("127.0.0.1", 53643)
        result_of_check = a_socket.connect_ex(location)
        if result_of_check == 0:
            external_ip = urllib.request.urlopen(
                'https://ident.me').read().decode('utf8')
            msg = f"""Server is up!
    byond://{external_ip}:53643"""
            await ctx.send(msg)
        else:
            msg = "Server is down!"
            await ctx.send(msg)
        a_socket.close()


def setup(client):
    client.add_cog(Server_commands(client))
