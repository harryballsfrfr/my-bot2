import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Needed to detect boosts
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_member_update(before, after):
    # Detect when user starts boosting
    if before.premium_since is None and after.premium_since is not None:
        channel = discord.utils.get(after.guild.text_channels, name='general')  # Change if needed
        if channel:
            await channel.send(f"🚀 Shoutout {after.mention} for boosting the server!")

bot.run("YOUR_BOT_TOKEN")
