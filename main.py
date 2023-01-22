from os import system
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Your Account ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

def update_title(title: str):
    system("title " + title)

update_title('Disclone - Getting info..')

print(f"""{Fore.MAGENTA}


████████████████████████████████████████████████
█▄─▄▄▀█▄─▄█─▄▄▄▄█─▄▄▄─█▄─▄███─▄▄─█▄─▀█▄─▄█▄─▄▄─█
██─██─██─██▄▄▄▄─█─███▀██─██▀█─██─██─█▄▀─███─▄█▀█
▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀

{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by Ripples.{Style.RESET_ALL}
        """)
token = input(f'🔮 Enter your Discord User\'s token 🔮:\n >')
guild_s = input('🔮 Now, give me the Guild ID You\'d like to copy 🔮:\n >')
guild = input('🔮 Right, what\'s the Guild ID to copy that server to? (You\'ve gotta own the server!) 🔮:\n >')


print("  ")
print("  ")

@client.event
async def on_ready():    
    update_title(f'Disclone - Using {client.user}.')

    print("NOTE: I\'ve had to make this slower so my goofy ahh doesn\'t get rate limited. This'll be a little slow.")
    
    print("Cloning, give me a few minutes..")
    guild_from = client.get_guild(int(guild_s))
    guild_to = client.get_guild(int(guild))

    update_title(f'Disclone - Editing Target')
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    
    update_title(f'Disclone - Cloning Roles to Target')
    await Clone.roles_create(guild_to, guild_from)
    
    update_title(f'Disclone - Cloning Categories to Target')
    await Clone.categories_create(guild_to, guild_from)
    
    update_title(f'Disclone - Cloning Channels to Target')
    await Clone.channels_create(guild_to, guild_from)
    
    update_title('Disclone - Finished')
    
    print(f"""{Fore.GREEN}
            Cloned! Check your guild to see if it failed.
    {Style.RESET_ALL}""")

    # await asyncio.sleep(5)
    await client.close()


client.run(token)