import discord
from discord.ext import commands
import asyncio

import os
import traceback

client = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@client.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
