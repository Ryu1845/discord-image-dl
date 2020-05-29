import discord, asyncio
import os

token=""
client = discord.Client()
print('Enter channelID')
channelID=int(input())
@client.event
async def on_connect():
    channel=client.get_channel(channelID)
    if not os.path.exists(channel.name):
        os.mkdir(channel.name)
    os.chdir(channel.name)
    async for message in channel.history():
        for attachment in message.attachments:
            await attachment.save(attachment.filename)
            print(attachment.filename)
    loop=asyncio.get_event_loop()
    loop.stop()
client.run(token, bot=False)
