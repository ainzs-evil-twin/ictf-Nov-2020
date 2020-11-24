"""
A discord bot for the challenge flag-sequencing on iCTF server.
"""

# import asyncio
import random
import discord
from discord.ext import commands

FLAG_TEXT = '<REDACTED>'

with open('token.txt', 'r') as f:
    TOKEN = f.read()

INTENTS = discord.Intents.default()

BOT = commands.Bot(command_prefix=';', intents=INTENTS)
BOT.remove_command('help')

def encode_to_decimal(text):
    """
    Encodes ASCII text to decimal equivalent
    """
    return int.from_bytes(text.encode('utf-8'), byteorder='big')

def generate_complimentary_strand(strand):
    """
    Generates a strand complimentary to any given strand
    """
    # <REDACTED>

def decimal_to_base_5(decimal):
    """
    Converts a decimal number to base 5
    """
    b5_integer = ''
    while decimal:
        b5_integer = str(decimal % 5) + b5_integer
        decimal = decimal//5
    return int(b5_integer)

def generate_all_fragments(strand):
    """
    Given a strand, generates all possible fragments
    """
    fragments = [strand]
    for i in range(1, len(str(strand))):
        fragments.append(strand//pow(10, i))
    return fragments

FLAG_DECIMAL = encode_to_decimal(FLAG_TEXT)
COMPLIMENTARY = generate_complimentary_strand(FLAG_DECIMAL)
FLAG_B5 = decimal_to_base_5(COMPLIMENTARY)
FRAGMENTS = generate_all_fragments(FLAG_B5)



@BOT.event
async def on_ready():
    """Notifies that the bot is running"""
    print(f'Logged in as {BOT.user}')
    await BOT.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name=";help"))

@BOT.command()
async def help(ctx):
    """Opens the list of commands"""
    embed = discord.Embed(
        colour=discord.Colour.orange())
    embed.set_author(name='Help : Commands')
    embed.add_field(name=';tube0', value='Random fragment from tube 0', inline=False)
    embed.add_field(name=';tube1', value='Random fragment from tube 1', inline=False)
    embed.add_field(name=';tube2', value='Random fragment from tube 2', inline=False)
    embed.add_field(name=';tube3', value='Random fragment from tube 0', inline=False)
    embed.add_field(name=';tube4', value='Random fragment from tube 0', inline=False)
    await ctx.send(embed=embed)

@BOT.event
async def on_command_error(ctx, error):
    """Shows the error message on discord itself"""
    await ctx.send(f'An error occurred: {error}')

@BOT.command()
async def tube0(ctx):
    """
    Retuns the length of one random fragment in tube-0
    """
    while True:
        random_index = random.randrange(0, len(FRAGMENTS))
        if str(FRAGMENTS[random_index])[-1] == '0':
            result = len(str(FRAGMENTS[random_index]))
            break
    await ctx.send(result)

@BOT.command()
async def tube1(ctx):
    """
    Retuns the length of one random fragment in tube-1
    """
    while True:
        random_index = random.randrange(0, len(FRAGMENTS))
        if str(FRAGMENTS[random_index])[-1] == '1':
            result = len(str(FRAGMENTS[random_index]))
            break
    await ctx.send(result)

@BOT.command()
async def tube2(ctx):
    """
    Retuns the length of one random fragment in tube-2
    """
    while True:
        random_index = random.randrange(0, len(FRAGMENTS))
        if str(FRAGMENTS[random_index])[-1] == '2':
            result = len(str(FRAGMENTS[random_index]))
            break
    await ctx.send(result)

@BOT.command()
async def tube3(ctx):
    """
    Retuns the length of one random fragment in tube-3
    """
    while True:
        random_index = random.randrange(0, len(FRAGMENTS))
        if str(FRAGMENTS[random_index])[-1] == '3':
            result = len(str(FRAGMENTS[random_index]))
            break
    await ctx.send(result)

@BOT.command()
async def tube4(ctx):
    """
    Retuns the length of one random fragment in tube-4
    """
    while True:
        random_index = random.randrange(0, len(FRAGMENTS))
        if str(FRAGMENTS[random_index])[-1] == '4':
            result = len(str(FRAGMENTS[random_index]))
            break
    await ctx.send(result)

BOT.run(TOKEN)
