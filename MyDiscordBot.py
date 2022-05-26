from discord.ext.commands import bot
from discord import DMChannel
import discord

token = ' '  # input your bot token here
client = discord.Client()
ID = 123  # input your id here instead of "123"
channel_id = 123  # input channel id that the bot will operate in instead of "123"


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user = await client.fetch_user(ID)
    if (message.author != user) and (message.author.bot is False):
        if message.channel.id == channel_id:
            await DMChannel.send(user, message.content)
    elif (message.author == user) and (message.channel.id != channel_id):
        message.channel.id = channel_id
        await message.channel.send(message.content)

client.run(token)
