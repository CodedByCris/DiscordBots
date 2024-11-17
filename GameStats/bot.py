import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure bots. Intents are required to access certain events.
intents = discord.Intents.default()
bot_fn = commands.Bot(command_prefix="fn!", intents=intents)
bot_vl = commands.Bot(command_prefix="vl!", intents=intents)

@bot_fn.event
async def on_ready():
    print(f"{bot_fn.user.name} has connected to Discord!")

@bot_vl.event
async def on_ready():
    print(f"{bot_vl.user.name} has connected to Discord!")

@bot_fn.command(name="ping")
async def ping_fn(ctx):
    await ctx.send("Pong from Fortnite bot!")

@bot_vl.command(name="ping")
async def ping_vl(ctx):
    await ctx.send("Pong from Valorant bot!")

# Run bots
bot_fn.run(TOKEN)
bot_vl.run(TOKEN)