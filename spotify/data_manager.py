import csv
import logging
import sys
import os
from get_path import DATA_TRACK_PATH
from spotify.class_track import Track


def data_manager(offset, artist, name, album_name, genre, url_spotify, preview):
    with open(DATA_TRACK_PATH, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([offset, name, artist,  album_name, genre, url_spotify, preview])


def last_index():
    with open(DATA_TRACK_PATH, mode='r', encoding='utf-8', newline='') as f:
        length = len(f.readlines())
        return length


def get_list_artists(form=None):
    list_artists = []
    if form == 'discord':
        for track in get_data_tracks():
            list_artists.append(track.artist.replace(' ', '-').lower())
    else:
        for track in get_data_tracks():
            if track.artist not in list_artists:
                list_artists.append(track.artist)
    return sorted(list_artists)


def get_data_tracks():
    list_tracks = []
    with open(DATA_TRACK_PATH, encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:  # Maybe you can do this simpler
            name = row[1]
            artist = row[2]
            album_name = row[3]
            genre = row[4]
            url_spotify = row[5]
            preview = row[6]
            list_tracks.append(Track(name, artist, album_name, genre, url_spotify, preview))
        list_tracks = sorted(list_tracks, key=lambda x: x.artist)
    return list_tracks


def get_data_per_artist(requested_artist=None, request='name'):
    list_artist = [track.artist for track in get_data_tracks()]
    list_ = [getattr(track, request) for track in get_data_tracks()]
    data_list = []
    for artist, data in zip(list_artist, list_):
        if artist.replace(' ', '-').lower() == requested_artist or artist == requested_artist:
            data_list.append(data)
        return data_list
        # return sorted(data_list)
