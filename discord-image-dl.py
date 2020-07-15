import discord, asyncio
import os
import requests

token=""
client = discord.Client()
wd=os.getcwd()
print('Enter channelID')
channelID=int(input())
if not os.path.exists(f"{channelID}.history"):
    os.mknod(f"{channelID}.history")
with open(f"{channelID}.history", "r") as f:
    history1 = f.readlines()

@client.event
async def on_connect():
    print('-------------------')
    channel=client.get_channel(channelID)
    print(f"Downloading #{channel.name}")
    if not os.path.exists(channel.name):
        os.mkdir(channel.name)
    os.chdir(channel.name)
    async for message in channel.history():
        file1 = open(os.path.join(wd, f"{channelID}.history"))
        if not f"{message.id}\n" in history1: 
            for attachment in message.attachments:
                print(attachment.url)
                await attachment.save(str(message.id))
            for embed in message.embeds:
                if embed.image.url is not embed.Empty:
                    print(embed.image.url)
                    image_url=embed.image.url
                    filename = str(message.id)
                    print(filename)
                    img_data = requests.get(image_url).content
                    with open(filename, 'wb') as handler:
                        handler.write(img_data)
            file1.write(f"{message.id}\n")             
    loop=asyncio.get_event_loop()
    loop.stop()
    file1.close()
client.run(token, bot=False)
