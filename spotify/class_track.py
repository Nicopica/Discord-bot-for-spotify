from dataclasses import dataclass


@dataclass()
class Track:
    name: str
    artist: str
    album_name: str
    genre: str
    url_spotify: str
    preview: str


class Artist:
    name: str
    url: str
    image: str
    info: str


class Album:
    name: str
    url: str
    image: str



