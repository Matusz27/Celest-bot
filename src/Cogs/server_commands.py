import socket, urllib.request
from discord.ext import commands


class Server_commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def servers(self, ctx):

        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        external_ip = urllib.request.urlopen(
            'https://ident.me').read().decode('utf8')

        location1 = ("127.0.0.1", 53643)
        location2 = ("192.168.1.17", 25565)

        result_of_check1 = a_socket.connect_ex(location1)
        result_of_check2 = a_socket.connect_ex(location2)

        msg = "Servers that are up: \n \n"

        if result_of_check1 == 0:
            msg += f"""Byond is up! \nURL: byond://{external_ip}:53643\n \n"""
        else:
            msg += f"""Byond is down! \n \n"""

        if result_of_check2 == 0:
            msg += f"""Minecraft is up! \nIP: {external_ip}:25565"""
        else:
            msg += f"""Minecraft is down!"""
            
        a_socket.close()
        await ctx.send(msg)
        


def setup(client):
    client.add_cog(Server_commands(client))
