#=- Discord.py bot
import random
import discord 

client = discord.Client()

commands_prefix = ':'

##== SIMPLE LIST TO PRINT IN CHAT ==##

question = [
    'Place question here',
    'Place question here',
]

##== Prints the bots username when the code is running ==##
    
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    
    msg = message.content
    
    ## Message using prefix ( not linked to list ) ##
    
    if msg.startswith(f'{commands_prefix}MESSAGEHERE'):
        embed = discord.Embed(
            title='TITLE HERE',
            description='Desc here', # Use /n if your wanting a new line in the description
            color=0x00000, # Use hex codes for the embed color #
        )
        embed.add_field(name="name", value="place text here", inline=True)
        await message.channel.send(embed=embed)
        
    #### Use the prefix to print the question ####
    
    if msg.startswith(f'{commands_prefix}question'):
        await message.channel.send(random.choice(question))