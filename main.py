import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True  # Needed to read messages

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_member_update(before, after):
    if before.premium_since is None and after.premium_since is not None:
        channel = discord.utils.get(after.guild.text_channels, name='general')
        if channel:
            await channel.send(f"🚀 Shoutout {after.mention} for boosting the server!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # If message includes 'ybnba' (case insensitive), react ✅
    if 'ybnba' in message.content.lower():
        try:
            await message.add_reaction('✅')
        except discord.errors.Forbidden:
            print("⚠️ Missing permissions to add reactions.")

    await bot.process_commands(message)  # Allows other commands to work
