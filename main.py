# bot.py
import os
import datetime
import discord
from dotenv import load_dotenv
from replit import db

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

template = 'Team : \nTop : {0}\nJungle : {1}\nMid : {2}\nAdc : {3}\nSupport : {4}'

async def manage_reaction(reaction):
  reac_t = ''
  reac_j = ''
  reac_m = ''
  reac_a = ''
  reac_s = ''

  print('__')

  # For each reaction in our message
  for reaction in reaction.message.reactions:
    async for user in reaction.users():
      if user != client.user:
        print(datetime.datetime.now(), user, reaction)

        if reaction.emoji == '🇹':
          reac_t += user.mention
        if reaction.emoji == '🇯':
          reac_j += user.mention
        if reaction.emoji == '🇲':
          reac_m += user.mention
        if reaction.emoji == '🇦':
          reac_a += user.mention
        if reaction.emoji == '🇸':
          reac_s += user.mention

  await reaction.message.edit(content=template.format(reac_t, reac_j, reac_m, reac_a, reac_s))

  #print(await Reaction.users())
  #print(Reaction.message.reactions)
  #print(Reaction.message.author == client.user)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == 'test' and (message.content == '!clash' or message.content == '!'):
    
      response = template.format('', '', '', '', '')

      msg = await message.channel.send(response)

      await msg.add_reaction('🇹')
      await msg.add_reaction('🇯')
      await msg.add_reaction('🇲')
      await msg.add_reaction('🇦')
      await msg.add_reaction('🇸')

      db["msg_id"] = msg.id


@client.event
async def on_reaction_add(reaction, user):
  await manage_reaction(reaction)


@client.event
async def on_raw_reaction_remove(payload):
  print('')
  #if (payload.message_id == db["msg_id"]):


client.run(TOKEN)