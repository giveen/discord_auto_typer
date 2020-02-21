#Run this from a terminal/command prompt. It will request you enter what you want to say and how many times
#you want it to say it.

import discord, sys, time, asyncio

token = ("DISCORD_LOGIN_TOKEN_FOR_PERSONAL_ACCOUNT_HERE")
client = discord.Client()
txt = str(input("Enter in spam text:"))
spamamt = int(input("Enter the amt of spam u want:"))


@client.event
async def on_ready():
    print("Bot is ready.")

#In the below 'if' statement, if a certain word is mention, the bot will begin spamming the message.
@client.event
async def on_message(message):
    if "spam" in message.content.lower():
        for x in range(0, spamamt):
            await message.channel.send(f'{txt}')
            await asyncio.sleep(65) #adjust this amount to the amount of seconds between each message

client.run(token, bot=False)
