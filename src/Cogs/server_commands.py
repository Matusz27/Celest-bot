import socket, requests
import database_handle
from discord.ext import commands


class Server_commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def servers(self, ctx):

        await ctx.send("Please wait, Checking...")
        
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        external_ip = requests.get('https://ident.me').text
        
        list_of_servers = database_handle.fetch_servers()   
        
        msg = "Servers Status: \n \n"
        
        for server in list_of_servers:
            
            await ctx.send(f"Checking status of {server['name']}...")
            
            location = (server['ip'], server['port'])
            result_of_check = a_socket.connect_ex(location)
            
            if result_of_check == 0:
                msg += f"""{server['name']} Online!\n {external_ip}:{server['port']}\n\n"""
                continue
            msg += f"""{server['name']} Offline!\n\n"""
            
        a_socket.close()
        await ctx.send(msg)
        


def setup(client):
    client.add_cog(Server_commands(client))
