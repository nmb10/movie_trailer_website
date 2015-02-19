#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fresh_tomatoes import open_movies_page
from models import Movie

# create list with my favorite movies
my_movies = [
    Movie(
        title='Game of Thrones',
        poster_image_url='http://ia.media-imdb.com/images/M/MV5BMTk0NDg4NjQ5N15BMl5BanBnXkFtZTgwMzkzNTgyMTE@._V1_SX214_AL_.jpg',
        trailer_youtube_url='http://www.youtube.com/watch?v=BpJYNVhGf1s',
        imdb_url='http://www.imdb.com/title/tt0944947/'
    ),
    Movie(
        title='The Big Lebowski',
        poster_image_url='http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_SX214_AL_.jpg',
        trailer_youtube_url='http://www.youtube.com/watch?v=cd-go0oBF4Y',
        imdb_url='http://www.imdb.com/title/tt0118715/'
    ),
    Movie(
        title='Napoleon Dynamite',
        poster_image_url='http://ia.media-imdb.com/images/M/MV5BNjYwNTA3MDIyMl5BMl5BanBnXkFtZTYwMjIxNjA3._V1_SX214_AL_.jpg',
        trailer_youtube_url='http://www.youtube.com/watch?v=ZHDi_AnqwN4',
        imdb_url='http://www.imdb.com/title/tt0374900/'
    ),
    Movie(
        title='Pulp Fiction',
        poster_image_url='http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg',
        trailer_youtube_url='http://www.youtube.com/watch?v=s7EdQ4FqbhY',
        imdb_url='http://www.imdb.com/title/tt0110912/'
    ),
    Movie(
        title='Groundhog Day',
        poster_image_url='http://ia.media-imdb.com/images/M/MV5BMTU0MzQyNTExMV5BMl5BanBnXkFtZTgwMjA0Njk1MDE@._V1_SX214_AL_.jpg',
        trailer_youtube_url='http://www.youtube.com/watch?v=tSVeDx9fk60',
        imdb_url='http://www.imdb.com/title/tt0107048/'
    )
]

# now generate html with my favorites and open in the browser
open_movies_page(my_movies)
