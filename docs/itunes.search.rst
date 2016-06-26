itunes.search module
====================

.. automodule:: itunes.search
    :members:
    :undoc-members:
    :show-inheritance:


Example Usage
-------------
The itunes.search module is made up of a handful of different utility functions
for performing a variety of different searches against the iTunes Store API.


Artist
^^^^^^
Searching for an artist is as simple as passing an artist name to the
`search_artist` function
::

    >>> import itunes
    >>> results = itunes.search_artist('Frank Sinatra')
    >>> frank = results[0]
    >>> frank
    ... '<Artist>: Frank Sinatra'


Albums
^^^^^^
To find an artist's albums, you can either use the `search_album` or access all
of an artists albums via an :class:`Artist` instance. Continuing from our above
example we could do something similar to::

  >>> for album in frank.get_albums():
  ...   print(album)
  ... <Collection>: Nothing But the Best (Remastered)
  ... <Collection>: Ultimate Sinatra
  ... <Collection>: Christmas With the Rat Pack
  ... <Collection>: Christmas
  ... <Collection>: A Jolly Christmas from Frank Sinatra (50th Anniversary)
  ... <Collection>: Sinatra At the Sands
  ... <Collection>: Classic Sinatra: His Great Performances 1953-1960
  ... ...


Apps
^^^^
Apps available from the iTunes store are also available for searching::

  >>> app = itunes.search_app('angry birds')[0]
  >>> app.ratings
  ... {'avg': {'all': 4.5,
               'current': 4.0},
       'num': {'all': 823399,
               'current': 504}}


TV Shows
^^^^^^^^
TV Shows are also searchable::

  >>> s1 = itunes.search_season('Family Guy Season 1')[0]
  >>> s1.release_date
  ... datetime.datetime(1999, 1, 31, 8, 0)
  >>> s1.artwork
  ... {'60': 'http://is1.mzstatic.com/image/thumb/Music3/v4/60/15/b2/6015b219-e4cb-2a93-0369-c75b5e06e9df/source/60x60bb.jpg',
       '600': 'http://is1.mzstatic.com/image/thumb/Music3/v4/60/15/b2/6015b219-e4cb-2a93-0369-c75b5e06e9df/source/600x600bb.jpg'}
  >>> s1.genre
  ... 'Comedy'
