#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Movie(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url, imdb_url, release_date):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_url = imdb_url
        self.release_date = release_date


my_movies = [
    Movie(
        'Game of the thrones',
        'http://ia.media-imdb.com/images/M/MV5BMTk0NDg4NjQ5N15BMl5BanBnXkFtZTgwMzkzNTgyMTE@._V1_SX214_AL_.jpg',
        'http://www.youtube.com/watch?v=BpJYNVhGf1s',
        '',
        ''
    ),
    Movie(
        'The Big Lebowski',
        'http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_SX214_AL_.jpg',
        'http://www.youtube.com/watch?v=cd-go0oBF4Y',
        '',
        ''
    ),
    Movie(
        'Napoleon Dynamite',
        'http://ia.media-imdb.com/images/M/MV5BNjYwNTA3MDIyMl5BMl5BanBnXkFtZTYwMjIxNjA3._V1_SX214_AL_.jpg',
        '',
        '',
        ''
    ),
    Movie(
        'Pulp Fiction',
        'http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg',
        '',
        '',
        ''
    ),
    Movie(
        'Groundhog Day',
        'http://ia.media-imdb.com/images/M/MV5BMTU0MzQyNTExMV5BMl5BanBnXkFtZTgwMjA0Njk1MDE@._V1_SX214_AL_.jpg',
        '',
        '12 February 1993',
        ''
    ),
]

from fresh_tomatoes import open_movies_page
open_movies_page(my_movies)
