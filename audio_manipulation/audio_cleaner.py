import sys
import os
from pydub import AudioSegment
from pytube import Search
import asyncio
import discord_bot.discord_bot
from multiprocessing import Pool
from get_path import DOWNLOAD_PATH
# from discord_bot.discord_bot import bot

OUTPUT_FORMAT = '.mp3'


def download_list(artist, list_pieces):
    artist_folder_path = os.path.join(DOWNLOAD_PATH, artist)

    def search_download(to_search):
        to_download = Search(artist.replace('-', ' ') + " " + to_search).results[0]  # select first result
        output_filename = to_download.streams.first().default_filename[:-5] + OUTPUT_FORMAT  # set output name
        output_path = os.path.join(DOWNLOAD_PATH, artist)
        to_download.streams.get_audio_only().download(output_path=output_path, filename=output_filename)  # download
        print(f'Downloading {to_download.title}')

    def silence_remover(audio_file, last_search):
        pass

    def regulate_volume(audio_file):
        pass

    def convert_file_format():  # maybe don't ?
        pass

    if not os.path.isdir(artist_folder_path):
        os.mkdir(os.path.join(DOWNLOAD_PATH, artist))

    progress = 0
    # print(os.path.join('C:\\Users\\Nico\\Desktop\\Authors', (author + '.txt')))
    print(list_pieces)
    print(artist)
    for piece in list_pieces:
        progress += 1
        print(str(round(progress / len(list_pieces) * 100, 2)) + "% completed")
        print(f'Progress:{progress} / {len(list_pieces)}')
        search_download(piece)
        # asyncio.run(search_download(piece))

# a = ['II. Andante cantabile con variazioni', 'Violin Romance No. 1 In G Major, Op. 40', 'Grosse Fuge in B Flat Major, Op. 133', 'Beethoven: Symphony No. 6 in F Major, Op. 68 "Pastoral": I. Erwachen heiterer Empfindungen bei der Ankunft auf dem Lande. Allegro ma non troppo', 'Symphony No. 7 in A Major, Op. 92: IV. Allegro con brio', 'Symphony No. 9 in D Minor, Op. 125 "Choral": III. Adagio molto e cantabile', 'Beethoven: Symphony No. 2 in D Major, Op. 36: III. Scherzo. Allegro', 'Symphony No. 4 in B-Flat Major, Op. 60: III. Allegro molto e vivace - Trio. Un poco meno allegro', 'Symphony No. 3 in E-Flat Major, Op. 55 "Eroica": III. Scherzo. Allegro vivace', 'Symphony No. 9 In D Minor, Op. 125 - "Choral": 2. Molto vivace', 'Symphony No. 9 In D Minor, Op. 125 - "Choral": 1. Allegro ma non troppo, un poco maestoso', 'Symphony No. 9 In D Minor, Op. 125 - "Choral" / 4.: "O Freunde nicht diese Töne" -', 'Symphony No. 9 In D Minor, Op. 125 - "Choral" - Excerpt From 4th Movement: 4. Presto', 'Symphony No. 9 In D Minor, Op. 125 - "Choral": 3. Adagio molto e cantabile', 'Symphony No. 5 in C Minor, Op. 67: I. Allegro con brio', 'Symphony No. 2 in D Major, Op. 36: I. Adagio molto - Allegro con brio', 'Symphony No. 2 in D Major, Op. 36: III. Scherzo..Allegro', 'Symphony No. 3 In E Flat, Op. 55 -"Eroica": 1. Allegro con brio', 'Symphony No. 3 In E Flat, Op. 55 -"Eroica": 2. Marcia funebre (Adagio assai)', 'Symphony No. 3 In E Flat, Op. 55 -"Eroica": 3. Scherzo (Allegro vivace)', 'Wind Quintet in E-Flat Major, Hess 19: II. Adagio maestoso', 'String Quartet No. 13 in B-Flat Major, Op. 130: II. Presto', 'Piano Sonata No. 8 In C Minor, Op. 13 -"Pathétique": 2. Adagio cantabile - Live', 'Piano Sonata No. 14 in C-Sharp Minor, Op. 27 No. 2 - "Moonlight": III. Presto agitato', 'Piano Sonata No. 17 in D Minor, Op. 31, No. 2, "Tempest": III. Allegretto', 'Piano Sonata No. 14 In C Sharp Minor, Op. 27 No. 2 -: I. Adagio sostenuto', 'Piano Sonata No. 8 in C Minor, Op. 13 "Pathétique": I. Grave - Allegro di molto e con brio', 'Piano Sonata No. 8 in C Minor, Op. 13 "Pathétique": II. Adagio cantabile', 'Piano Sonata No. 8 in C Minor, Op. 13 "Pathétique": III. Rondo (Allegro)', 'Piano Sonata No. 14 in C-Sharp Minor, Op. 27 No. 2 - "Moonlight": I. Adagio sostenuto', 'Piano Sonata No. 14 in C-Sharp Minor, Op. 27 No. 2 - "Moonlight": II. Allegretto', 'Piano Sonata No. 17 In D Minor, Op. 31, No. 2 -"The Tempest": 1. Largo - Allegro', 'Piano Sonata No. 17 In D Minor, Op. 31, No. 2 -"The Tempest": 3. Allegretto', 'Piano Sonata No. 17 In D Minor, Op. 31, No. 2 -"The Tempest": 2. Adagio', 'Piano Sonata No. 20 In G Major, Op. 49, No. 2: 1. Allegro ma non troppo', 'Piano Sonata No. 20 In G Major, Op. 49, No. 2: 2. Tempo di Menuetto', 'Piano Sonata No. 21 In C, Op. 53 -"Waldstein": 1. Allegro con brio', 'Piano Sonata No. 21 In C, Op. 53 -"Waldstein": 2. Introduzione (Adagio molto)', 'Piano Sonata No. 21 In C, Op. 53 -"Waldstein": 3. Rondo (Allegretto moderato - Prestissimo)', 'Piano Sonata No. 23 in F Minor, Op. 57 "Appassionata": I. Allegro assai', 'Piano Sonata No. 23 in F Minor, Op. 57 "Appassionata": II. Andante con moto', 'Piano Sonata No. 23 in F Minor, Op. 57 "Appassionata": III. Allegro ma non troppo', 'Piano Concerto No. 4 in G Major, Op. 58: I. Allegro moderato', 'Piano Concerto No. 2 in B Flat Major, Op. 19: II. Adagio', 'Piano Concerto No. 5 in E-Flat Major, Op. 73: II. Adagio un poco mosso', 'Piano Concerto No. 5 in E Flat Major, Op. 73 "Emperor": II. Adagio un poco mosso', 'Egmont, Op. 84: Overture', 'Fidelio, Op. 72: Overture', 'Bagatelle No. 25 in A Minor, WoO 59 "Für Elise"']
# b = 'ludwig-van-beethoven'
# download_list(b, a)
