import os
import discord
from dotenv import load_dotenv
from replit import db
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

template = 'Team : \nTop : {0}\nJungle : {1}\nMid : {2}\nAdc : {3}\nSupport : {4}'

async def manage_reaction(message):
  reac_t = ''
  reac_j = ''
  reac_m = ''
  reac_a = ''
  reac_s = ''

  # For each reaction in our message
  for reaction in message.reactions:
    async for user in reaction.users():
      if user != client.user:

        if reaction.emoji == '🇹':
          if reac_t != '':
            reac_t += '/'
          reac_t += user.mention

        if reaction.emoji == '🇯':
          if reac_j != '':
            reac_j += '/'
          reac_j += user.mention

        if reaction.emoji == '🇲':
          if reac_m != '':
            reac_m += '/'
          reac_m += user.mention

        if reaction.emoji == '🇦':
          if reac_a != '':
            reac_a += '/'
          reac_a += user.mention

        if reaction.emoji == '🇸':
          if reac_s != '':
            reac_s += '/'
          reac_s += user.mention

  await reaction.message.edit(content=template.format(reac_t, reac_j, reac_m, reac_a, reac_s))


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.channel.name == 'test' or message.channel.name == 'lol-clash') and message.content == '!clash':
    
      response = template.format('', '', '', '', '')

      msg = await message.channel.send(response)

      await msg.add_reaction('🇹')
      await msg.add_reaction('🇯')
      await msg.add_reaction('🇲')
      await msg.add_reaction('🇦')
      await msg.add_reaction('🇸')

      db["msg_id"] = msg.id
      db["channel_id"] = msg.channel.id


#@client.event
#async def on_reaction_add(reaction, user):
#  if user != client.user:
#    await manage_reaction(reaction.message)


@client.event
async def on_raw_reaction_add(payload):
  channel = client.get_channel(db['channel_id'])
  message = await channel.fetch_message(db['msg_id'])

  await manage_reaction(message)


@client.event
async def on_raw_reaction_remove(payload):
  channel = client.get_channel(db['channel_id'])
  message = await channel.fetch_message(db['msg_id'])

  await manage_reaction(message)


keep_alive()
client.run(TOKEN)