import asyncio
import os

import discord
import requests

token = "NzkxMTIwOTA1NjUxNjE3ODEy.YEIBMQ.k3TS-4aRHnnWBR38PR1U2bKfFPw"
client = discord.Client()
wd = os.getcwd()
print('Enter channel_id')
channel_id = int(input())
if not os.path.exists(f"{channel_id}.history"):
    os.mknod(f"{channel_id}.history")
with open(f"{channel_id}.history", "r") as f:
    history_file_lines = f.readlines()


@client.event
async def on_connect():
    print('-------------------')
    channel = client.get_channel(channel_id)
    print(f"Downloading #{channel.name}")
    if not os.path.exists(channel.name):
        os.mkdir(channel.name)
    os.chdir(channel.name)
    history_file = open(os.path.join(wd, f"{channel_id}.history"), 'a')
    async for message in channel.history():
        if f"{message.id}\n" not in history_file_lines:
            for attachment in message.attachments:
                print(attachment.filename)
                await attachment.save(str(attachment.filename))
            for embed in message.embeds:
                if embed.image.url is not embed.Empty:
                    print(embed.image.url)
                    image_url = embed.image.url
                    filename = image_url.split('/')[-1].split('?')[0]
                    print(filename)
                    img_data = requests.get(image_url).content
                    with open(filename, 'wb') as handler:
                        handler.write(img_data)
            history_file.write(f"{message.id}\n")
    loop = asyncio.get_event_loop()
    loop.stop()
    history_file.close()
client.run(token, bot=False)
