import discord, asyncio, sys
from discord.ext import commands
from datetime import datetime, timedelta

import os
import traceback

bot = commands.Bot(command_prefix='.')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 587605345942372352 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(626439869039771668)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)
            
            


@bot.command()
async def poll(ctx, about = "question", *args):
    emojis = ["1⃣","2⃣","3⃣","4⃣","5️⃣","6️⃣","7️⃣"]

    cnt = len(args)
    message = discord.Embed(title=":speech_balloon:アンケートです。 "+about,colour=0x1e90ff)
    if cnt <= len(emojis):
        for a in range(cnt):
            message.add_field(name=f'{emojis[a]}{args[a]}', value="** **", inline=False)
        msg = await ctx.send(embed=message)
        #投票の欄
        for i in range(cnt):
            await msg.add_reaction(emojis[i])
    else:
        await ctx.send("項目数上限オーバー")

bot.run(token)
