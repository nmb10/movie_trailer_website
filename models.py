#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Movie(object):
    """ Stores movie information.

    title (str): title of the movie
    poster_image_url (str): url of the image
    trailer_youtube_url (str): url of the trailer on youtube
    imdb_url (str): ulr of the movied details on imdb
    """

    def __init__(self, title=None, poster_image_url=None,
                 trailer_youtube_url=None, imdb_url=None):
        """ Initializes new movie.

        Args:
            title (str): title of the movie
            poster_image_url (str): url of the image
            trailer_youtube_url (str): url of the trailer on youtube
            imdb_url (str): ulr of the movied details on imdb

        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_url = imdb_url
        self.validate()

    def validate(self):
        """ Checks all fields for values. Raises exception if any field has no value. """

        # all fields are required. Check them.
        errors = []
        if not self.title:
            errors.append('title is required field')
        if not self.poster_image_url:
            errors.append('poster_image_url is required field')
        if not self.trailer_youtube_url:
            errors.append('trailer_youtube_url is required field')
        if not self.imdb_url:
            errors.append('imdb_url is required field')
        if errors:
            raise Exception('Empty field errors: %s' % ','.join(errors))
