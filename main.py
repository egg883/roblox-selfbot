#Sorry for the shit coding kinda rushed this


import time
import json
from discord.ext import commands
from roblox import Client
from colorama import Fore
import sys
import discord
import os
# ---------------------------------------- Imports
config = json.load(open('config.json', 'rb'))

prefix = config['prefix']
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')
def restart_bot(): 
  os.execv(sys.executable,sys.argv)
client1 = Client()
async def main():
    await client1.get_user(1)
def typingprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.00000000001)
def Clear():
    os.system('cls')
# ---------------------------------------- DEF

typingprint(f"Waiting for input prefix is {config['prefix']}")

@bot.command()
async def user(ctx, user):
    await ctx.message.delete()
    user1 = await client1.get_user_by_username(user)
    msg = f"""
```ini
Found info for {user1.name}

[Username: {user1.name}]
[Display name: {user1.display_name}]
[Creation date: {user1.created}]
[User ID: {user1.id}]
[Banned: {user1.is_banned}]
[Description:
{user1.description}]
```
    """
    await ctx.send(msg)

def Init():
    with open('config.json', encoding="utf-8") as f:
        config = json.load(f)
    token = config.get('token')
    try:
        bot.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        input(f"{Fore.RED}[SYSTEM] TOKEN IS INVALID CHECK CONFIG"+Fore.White)
        sys.exit
        python = sys.executable
        os.execl(python, python, * sys.argv)
Init()