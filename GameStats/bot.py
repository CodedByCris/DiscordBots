import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from messages import messages  # Import the messages

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure bot. Intents are required to access certain events.
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
intents.reactions = True  # Enable the reactions intent

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="stats", help="Select language for stats")
async def stats(ctx):
    # Send a message asking the user to select a language
    message = await ctx.send(messages["select_language"])
    # Add reactions for English and Spanish
    await message.add_reaction("🇬🇧")
    await message.add_reaction("🇪🇸")

@bot.event
async def on_reaction_add(reaction, user):
    # Ignore bot reactions
    if user.bot:
        return

    # Check if the reaction is from the bot
    if reaction.message.author != bot.user:
        return

    # Check if the reaction is from the correct message
    if reaction.emoji == "🇬🇧":
        if messages["select_language"] in reaction.message.content:
            # Send a message asking the user to select a game
            message = await reaction.message.channel.send(messages["select_game_en"])
            # Add reactions for Fortnite and Valorant
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
        elif messages["select_game_en"] in reaction.message.content:
            if "Fortnite" in reaction.message.content:
                # Send a message with information about the Fortnite bot
                await reaction.message.channel.send(messages["fortnite_info_en"])
            elif "Valorant" in reaction.message.content:
                # Send a message with information about the Valorant bot
                await reaction.message.channel.send(messages["valorant_info_en"])
    elif reaction.emoji == "🇪🇸":
        if messages["select_language"] in reaction.message.content:
            # Send a message asking the user to select a game
            message = await reaction.message.channel.send(messages["select_game_es"])
            # Add reactions for Fortnite and Valorant
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
        elif messages["select_game_es"] in reaction.message.content:
            if "Fortnite" in reaction.message.content:
                # Send a message with information about the Fortnite bot in Spanish
                await reaction.message.channel.send(messages["fortnite_info_es"])
            elif "Valorant" in reaction.message.content:
                # Send a message with information about the Valorant bot in Spanish
                await reaction.message.channel.send(messages["valorant_info_es"])
    elif reaction.emoji == "1️⃣":
        if messages["select_game_en"] in reaction.message.content:
            # Send a message with information about the Fortnite bot
            await reaction.message.channel.send(messages["fortnite_info_en"])
        elif messages["select_game_es"] in reaction.message.content:
            # Send a message with information about the Fortnite bot in Spanish
            await reaction.message.channel.send(messages["fortnite_info_es"])
    elif reaction.emoji == "2️⃣":
        if messages["select_game_en"] in reaction.message.content:
            # Send a message with information about the Valorant bot
            await reaction.message.channel.send(messages["valorant_info_en"])
        elif messages["select_game_es"] in reaction.message.content:
            # Send a message with information about the Valorant bot in Spanish
            await reaction.message.channel.send(messages["valorant_info_es"])

# Run bot
bot.run(TOKEN)