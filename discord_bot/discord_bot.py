import discord
from discord.ext import commands
from discord.utils import get
import os
import sys
import random
from spotify.data_manager import last_index
from spotify.spotify_utils import read_saved_tracks
import asyncio
from dotenv import load_dotenv
from audio_manipulation.audio_cleaner import download_list
from spotify.spotify_utils import get_image_composer
from audio_manipulation import audio_cleaner
from composers_classification import list_eras_authors, name_categories, get_era, all_possible_channels
from spotify.data_manager import get_data_tracks, get_list_artists, get_data_per_artist, last_index
from discord_bot.image_genre import generate_image
from discord_bot.get_information_ai import get_ai_description

load_dotenv()
TOKEN = os.getenv('TOKEN')
if not TOKEN:
    print('ERROR: Token var is missing: TOKEN')
    sys.exit(-1)
#
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    # await bot.loop.run_in_executor(None, read_saved_tracks)
    # await bot.loop.create_task(read_saved_tracks())
    # bot.loop.run_in_executor(None, read_saved_tracks)
    # await asyncio.run(await read_saved_tracks())
    # await read_saved_tracks()


@bot.command(name='h')
async def custom_help(ctx, *, name=None):
    print('help')
    await ctx.message.channel.send('Commands:\n'
                                   '*`!delete`*: deletes all channels besides general\n'
                                   '*`!create`*: not supported creates all composers channels and adds photo\n'
                                   '*`!add`*: not supported adds all liked compositions of every composer\n'
                                   '*`!creadd`*: create + add lmao\n'
                                   '*`!cl`*: cleans x messages of that channel\n'
                                   '*`!h`*: why  would you need to know this lol\n'
                                   '*`!dw`* download, only for me 🤓🤓🤓')


@bot.command(name='delete')
async def delete_all_channels(ctx, *, name=None):
    print('delete_all_channels')
    guild = ctx.message.guild
    for channel in guild.channels:
        if str(channel) in all_possible_channels:
            await channel.delete()
        else:
            print(f"Channel {channel} wasn't deleted")


@bot.command(name='creadd')
async def create_and_add(ctx, arg='album_name', name=None):
    print('creadd executed')
    guild = ctx.message.guild
    overwrites = {guild.default_role: discord.PermissionOverwrite(send_messages=False)}
    list_artist = [track.artist for track in get_data_tracks()]

    color_palette = [0xff0000, 0xffa500, 0xffff00, 0x008000, 0x0000ff, 0x4b0082, 0xee82ee]
    selected_color = 0

    list_class_track = get_data_tracks()
    for new_category in name_categories:  # Create categories
        if new_category not in str(guild.categories):
            await ctx.guild.create_category(new_category)

    for new_channel in list_artist:
        if new_channel.replace(' ', '-').lower() not in str(guild.channels):  # If channel doesn't exist
            category = discord.utils.get(ctx.guild.channels, name=get_era(new_channel))  # Create channel
            await guild.create_text_channel(name=new_channel, overwrites=overwrites, category=category)

            photo = get_image_composer(new_channel)
            description = get_ai_description(str(new_channel))
            created_channel = discord.utils.get(ctx.guild.channels, name=new_channel.replace(' ', '-').lower())

            # await created_channel.send(photo)  # Add photo
            # await created_channel.send(description)  # Add description

            embed = discord.Embed(title=str(new_channel), url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                                  description=description, color=0x000000)
            embed.set_thumbnail(url=photo)
            await created_channel.send(embed=embed)

            # Change text and pic for embed message and hyperlink to their spotify / wiki

            last_prop = ''
            for track_class in list_class_track[:]:
                print(len(list_class_track))
                if track_class.artist == new_channel:
                    title = track_class.name
                    url = track_class.url_spotify
                    if last_prop != getattr(track_class, arg) != 'not found':  # Album changed
                        if selected_color >= len(color_palette) - 1:
                            selected_color = 0
                        else:
                            selected_color += 1
                        await created_channel.send(file=discord.File(generate_image(getattr(track_class, arg))))
                    # color=color_palette[selected_color]   Change color of text presenting playlists
                    last_prop = getattr(track_class, arg)
                    embed = discord.Embed(title=title, url=url, color=color_palette[selected_color])
                    await created_channel.send(embed=embed)
                    list_class_track.remove(track_class)  # Delete elements already categorized

@bot.command(name='sug')
async def suggest(ctx, arg, name=None):
    await ctx.message.channel.send(
        f"Suggestion {arg} sent, if it's a troll suggestion be aware of the consequences")
    print(f'New suggestion: {arg}')


@bot.command(name='quiz')
async def quiz(ctx, arg, name=None):
    await ctx.message.channel.send('dev too lazy to do this', delete_after=15.0)
    # waiting time until delete message@bot.command(name='quiz')


@bot.command(name='update')
async def update_data(ctx, *, name=None):
    await ctx.message.delete()  # delete request command
    await ctx.message.channel.send('Updating data, wait until I finish', delete_after=15.0)
    await bot.loop.run_in_executor(None, read_saved_tracks)
    await ctx.message.channel.send(f'Length {last_index()} ', delete_after=15.0)


@bot.command(name='cl')
async def clean(ctx, arg, name=None):
    print('clean')
    await ctx.message.channel.send(f'Deleting {arg} messages')
    await ctx.channel.purge(limit=int(arg) + 2)


@bot.command(name='dw')
async def get_messages(ctx, *, name=None):
    print('download')
    await ctx.message.channel.send('Message received', delete_after=3.0)  # waiting time until delete message
    await ctx.message.delete()  # delete request command
    channel_name = str(ctx.message.channel)
    data = []
    async for msg in ctx.message.channel.history():
        msg.content = msg.content.rsplit('` |')[0].replace('`', '')
        if msg.content:
            data.append(msg.content)
    if data:
        data.pop(0)  # Filter photo, text and bot's received message
        data.pop()
        data.pop()
        await bot.loop.run_in_executor(None, download_list, channel_name, data)


@bot.command(name='test')
async def test(ctx, *, name=None):
    print('test')
    color_palette = [0xff0000, 0xffa500, 0xffff00, 0x008000, 0x0000ff, 0x4b0082, 0xee82ee]
    r = random.randint(0, 7)
    # color = '000000'
    color = 0
    # for i in range(256):
    #     color = '0x'
    #     color = color + "{:02x}".format(i)
    #     color = color + "{:02x}".format(i)
    #     color = color + '{:02x}'.format(i)
    #     print(color)

    for c in color_palette:
        embed = discord.Embed(title="Sample NAME OF A PIECE THAT IS long", color=c)
        await ctx.message.channel.send(embed=embed)


def run_bot():
    bot.run(TOKEN)
