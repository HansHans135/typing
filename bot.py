import discord
client = discord.Client()

@client.event   
async def on_ready():
    print('機器人已啟動，目前使用的bot：',client.user)

@client.event
async def on_message(message):
    if message.content == '.!typing':
        await message.channel.send('已開始漫長的輸入!(使用`.!stop`停止)')
        channel = message.channel
        async with message.channel.typing():
            def checkmessage(m):
                return m.content == '.!stop' and m.channel == channel
            msg = await client.wait_for('message', check=checkmessage)
            await channel.send('已停止漫長的輸入!(使用`.!typinp`再次開始)'.format(msg))


client.run("TOKEN放這裡") 
