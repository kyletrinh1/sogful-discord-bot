import discord # imports discord.py to run the libraries required.

client = discord.Client()

@client.event
async def on_ready(): # listens for client event using annotation, notifies console when logged in
    print('We have logged in as {0.user}'.format(client)) # yeah

@client.event
async def on_message(message):
    if message.author == client.user: 
        return
        # ensures the message received from the text channel the bot is not itself

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTAyNzA4MTEzOTQ4OTM0OTYzMg.G8HlxT.V_-vbNjOYyCUKfG0BmeWH8W0teiAVSvmkGFJfQ')