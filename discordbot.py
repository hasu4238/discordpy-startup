import discord, asyncio, random
from discord.ext import commands

import os
import traceback

client = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@client.command()
async def ping(ctx):
    await ctx.send('po2ng')


client.run(token)
