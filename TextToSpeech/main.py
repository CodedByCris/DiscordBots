import discord
from discord.ext import commands
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Configurar el bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Configurar el motor de TTS
engine = pyttsx3.init()

# Comando para unirse al canal de voz
@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("¡Me he unido al canal de voz!")
    else:
        await ctx.send("Debes estar en un canal de voz para invitarme.")

# Comando para salir del canal de voz
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("¡Me he desconectado del canal!")
    else:
        await ctx.send("No estoy conectado a ningún canal de voz.")

# Comando para convertir texto en voz
@bot.command()
async def say(ctx, *, text: str):
    if not ctx.voice_client:
        await ctx.send("Primero necesito estar en un canal de voz. Usa `!join`.")
        return

    # Convertir texto a archivo de audio
    audio_file = "tts_output.mp3"
    engine.save_to_file(text, audio_file)
    engine.runAndWait()

    # Reproducir el archivo en el canal de voz
    ctx.voice_client.stop()  # Detener cualquier audio en reproducción
    source = discord.FFmpegPCMAudio(audio_file)
    ctx.voice_client.play(source, after=lambda e: print(f"Reproducción finalizada: {e}"))
    await ctx.send("Reproduciendo texto en voz...")

# Manejar errores
@say.error
async def tts_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Por favor, incluye el texto que quieres convertir. Ejemplo: `!say Hola a todos`")

bot.run(DISCORD_TOKEN)
