import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

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
    message = await ctx.send("Select language for stats:\n\n🇬🇧 English\n\n🇪🇸 Español")
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
        if "Select language for stats" in reaction.message.content:
            # Send a message asking the user to select a game
            message = await reaction.message.channel.send("Select game for stats:\n\n1️⃣ Fortnite\n\n2️⃣ Valorant\n")
            # Add reactions for Fortnite and Valorant
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
        elif "Select game for stats" in reaction.message.content:
            if "Fortnite" in reaction.message.content:
                # Send a message with information about the Fortnite bot
                await reaction.message.channel.send("This is the Fortnite bot! It provides information and commands related to Fortnite.")
            elif "Valorant" in reaction.message.content:
                # Send a message with information about the Valorant bot
                await reaction.message.channel.send("This is the Valorant bot! It provides information and commands related to Valorant.")
    elif reaction.emoji == "🇪🇸":
        if "Select language for stats" in reaction.message.content:
            # Send a message asking the user to select a game
            message = await reaction.message.channel.send("Selecciona el juego para estadísticas:\n\n1️⃣ Fortnite\n\n2️⃣ Valorant\n")
            # Add reactions for Fortnite and Valorant
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
        elif "Selecciona el juego para estadísticas" in reaction.message.content:
            if "Fortnite" in reaction.message.content:
                # Send a message with information about the Fortnite bot in Spanish
                await reaction.message.channel.send("¡Este es el bot de Fortnite! Proporciona información y comandos relacionados con Fortnite.")
            elif "Valorant" in reaction.message.content:
                # Send a message with information about the Valorant bot in Spanish
                await reaction.message.channel.send("¡Este es el bot de Valorant! Proporciona información y comandos relacionados con Valorant.")
    elif reaction.emoji == "1️⃣":
        if "Select game for stats" in reaction.message.content:
            # Send a message with information about the Fortnite bot
            await reaction.message.channel.send("This is the Fortnite bot! It provides information and commands related to Fortnite.")
        elif "Selecciona el juego para estadísticas" in reaction.message.content:
            # Send a message with information about the Fortnite bot in Spanish
            await reaction.message.channel.send("¡Este es el bot de Fortnite! Proporciona información y comandos relacionados con Fortnite.")
    elif reaction.emoji == "2️⃣":
        if "Select game for stats" in reaction.message.content:
            # Send a message with information about the Valorant bot
            await reaction.message.channel.send("This is the Valorant bot! It provides information and commands related to Valorant.")
        elif "Selecciona el juego para estadísticas" in reaction.message.content:
            # Send a message with information about the Valorant bot in Spanish
            await reaction.message.channel.send("¡Este es el bot de Valorant! Proporciona información y comandos relacionados con Valorant.")

# Run bot
bot.run(TOKEN)