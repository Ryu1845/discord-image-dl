import discord, asyncio
import os
import requests

token=""
client = discord.Client()
print('Enter channelID')
channelID=int(input())
@client.event
async def on_connect():
    print('-------------------')
    channel=client.get_channel(channelID)
    print('Downloading '+channel.name+'\n')
    if not os.path.exists(channel.name):
        os.mkdir(channel.name)
    os.chdir(channel.name)
    async for message in channel.history():
        for attachment in message.attachments:
            await attachment.save(attachment.filename)
            print(attachment.filename)
        for embed in message.embeds:
            if embed.image.url is not embed.Empty:
                image_url=embed.image.url
                filename = image_url.split('/')[-1]
                print(filename)
                img_data = requests.get(image_url).content
                with open(filename, 'wb') as handler:
                    handler.write(img_data)             
    loop=asyncio.get_event_loop()
    loop.stop()
client.run(token, bot=False)
