import discord, asyncio
import os
import requests
wd=os.getcwd()
token=""
client = discord.Client()
print('Enter channelID')
channelID=int(input())
if not os.path.exists(str(channelID)+".history"):
    f=open(str(channelID)+".history","w")
    f.close()
file1=open(str(channelID)+".history","r") 
history1=file1.readlines()
file1.close()
@client.event
async def on_connect():
    print('-------------------')
    channel=client.get_channel(channelID)
    print('Downloading #'+channel.name+'\n')
    if not os.path.exists(channel.name):
        os.mkdir(channel.name)
    os.chdir(channel.name)
    async for message in channel.history():
        file1 = open(wd+"/"+str(channelID)+".history","a")
        if not str(message.id)+"\n" in history1: 
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
            file1.write(str(message.id)+"\n")             
    loop=asyncio.get_event_loop()
    loop.stop()
    file1.close()
client.run(token, bot=False)
