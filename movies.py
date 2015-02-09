#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fresh_tomatoes import open_movies_page


class Movie(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url, imdb_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_url = imdb_url


my_movies = [
    Movie(
        'Game of Thrones',
        'http://ia.media-imdb.com/images/M/MV5BMTk0NDg4NjQ5N15BMl5BanBnXkFtZTgwMzkzNTgyMTE@._V1_SX214_AL_.jpg',
        'http://www.youtube.com/watch?v=BpJYNVhGf1s',
        'http://www.imdb.com/title/tt0944947/'
    ),
    Movie(
        'The Big Lebowski',
        'http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_SX214_AL_.jpg',
        'http://www.youtube.com/watch?v=cd-go0oBF4Y',
        'http://www.imdb.com/title/tt0118715/'
    ),
    Movie(
        'Napoleon Dynamite',
        'http://ia.media-imdb.com/images/M/MV5BNjYwNTA3MDIyMl5BMl5BanBnXkFtZTYwMjIxNjA3._V1_SX214_AL_.jpg',
        'http://www.youtube.com/watch?v=ZHDi_AnqwN4',
        'http://www.imdb.com/title/tt0374900/'
    ),
    Movie(
        'Pulp Fiction',
        'http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg',
        'http://www.youtube.com/watch?v=s7EdQ4FqbhY',
        'http://www.imdb.com/title/tt0110912/'
    ),
    Movie(
        'Groundhog Day',
        'http://ia.media-imdb.com/images/M/MV5BMTU0MzQyNTExMV5BMl5BanBnXkFtZTgwMjA0Njk1MDE@._V1_SX214_AL_.jpg',
        'http://www.youtube.com/watch?v=tSVeDx9fk60',
        'http://www.imdb.com/title/tt0107048/'
    )
]

open_movies_page(my_movies)
