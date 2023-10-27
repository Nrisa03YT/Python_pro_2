import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    channel_id = 1152369673573244999
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''Hola! Soy el Bot de resumenes del UCM. 
                           Para ver la lista de películas escribe: UCM_F1.''')

@bot.command()
async def UCM_F1(ctx):
    await ctx.send('''Películas de la FASE 1 del UCM
                   F1 1: Capitán America
                   F1 2: Iron Man
                   F1 3: Thor
                   F1 4: Próximamente''')
    
@bot.command()
async def F1_1(ctx):
    await ctx.send('''Resumen Capitán America: https://www.youtube.com/watch?v=yTC-nC-BSSA''')

@bot.command()
async def F1_2(ctx):
    await ctx.send('''Resumen Iron Man: https://www.youtube.com/watch?v=NxJidPbMLhs''')

@bot.command()
async def F1_3(ctx):
    await ctx.send('''Resumen Thor: https://www.youtube.com/watch?v=nTfW-c4K1vo''')

@bot.command()
async def F1_4(ctx):
    await ctx.send('''Resumen "F1 4": Próximamente...''')

bot.run("MTE1OTk2ODAyNzkyODk2OTMwOA.Gv0JL_.DbOb9b8Z1-6UkUzyFvGziIesavTeNXl8uXiEv0")