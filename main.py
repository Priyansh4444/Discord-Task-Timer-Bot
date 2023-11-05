import os
import discord
import datetime
import asyncio
from keepalive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all()) 
user_data = {}
ud = ""
ur = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def wash(ctx):
    if ctx.author == client.user:
        return

    else:
        current_time = datetime.datetime.now().timestamp()
        await ctx.channel.send(f'Hello! The command was executed at: <t:{current_time:.0f}:R>')

        await asyncio.sleep(1800)

        current_time = datetime.datetime.now().timestamp()
        await ctx.channel.send(f'Hello  {ctx.message.author.mention}! 30 minutes have passed. The time is now: <t:{current_time:.0f}:R>')

@client.command()
async def dry(ctx):
    if ctx.author == client.user:
        return

    else:
        current_time = datetime.datetime.now().timestamp()
        await ctx.channel.send(f'Hello! The command was executed at: <t:{current_time:.0f}:R>')

        await asyncio.sleep(2700)

        current_time = datetime.datetime.now().timestamp()
        await ctx.channel.send(f'Hello  {ctx.message.author.mention}! 45 minutes have passed. The time is now: <t:{current_time:.0f}:R>')

@client.command()
async def vacuum(ctx, room_number: int):
    # Get the user's ID
    global ud
    global ur
    user_id = str(ctx.message.author.mention)
    if  ur == room_number or user_id == ud:
        user_data[ud] = [False, room_number]
        response = f"{user_id} from Room {ur}. Now {'has' if user_data[ud][0] else 'does not have'} evac hostage in that room."
        await ctx.send(response)

        ud = ""
        ur = 0
    elif ud != "":
        await ctx.channel.send(f'{ud} in {ur} has the vacuum')
        return
    else:
        user_data[user_id] = [True, room_number]
        ud = user_id
        ur = room_number
        response = f"{user_id} from Room {ur}. Now {'has' if user_data[ud][0] else 'no longer has'} evac hostage in that room."
        await ctx.send(response)
 
keep_alive()
client.run(os.environ['TOKEN'])