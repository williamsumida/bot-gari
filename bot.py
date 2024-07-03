from dotenv import load_dotenv
from discord import Message, TextChannel, Guild
from discord.ext import commands
from time import sleep
import discord
import logging
import os


load_dotenv()


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


intents = discord.Intents.all()


client = discord.Client(intents=intents)


async def delete_message(message: Message):
    await message.delete(delay=5.0)

bot = commands.Bot(command_prefix='!', intents=intents)

async def transport_message(message: Message, target_channel_id: int ):
    print(bot.get_guild())
    target_channel = bot.get_channel()

    if target_channel:
        await target_channel.send('This is a message sent to another channel!')
    else:
        await message.channel.send('Target channel not found.')

@client.event
async def on_ready():
    logger.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    if message.content.startswith(';pokemon'):
        await transport_message(message, TARGET_CHANNEL)
        await delete_message(message)
    else:
        await message.channel.send("oi")



DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN:
    client.run(DISCORD_TOKEN)

