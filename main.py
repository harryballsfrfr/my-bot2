import os
import discord
from discord.ext import commands
from aiohttp import web
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def handle(request):
    return web.Response(text="Bot is alive!")

app = web.Application()
app.add_routes([web.get('/', handle)])

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

async def run():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT', 8000)))
    await site.start()
    await bot.start(os.getenv("TOKEN"))

asyncio.run(run())
