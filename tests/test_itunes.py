# -*- coding: utf-8 -*-
import itunes
import pytest

U2 = 'U2'
U2_ONE = 'One'
U2_ACHTUNGBABY = 'Achtung Baby (Remastered)' # 'Achtung Baby'

U2_ONE_ID = 475387108 # Before it was 368617
U2_ACHTUNGBABY_ID = 475386884 # Before it was 368713
U2_ID = 78500

U2_URL = '{host}us/artist/u2/id{id}?uo=4'.format(host=itunes.HOST_NAME,
                                                 id=U2_ID)
U2_ACHTUNGBABY_URL = 'https://itunes.apple.com/us/album/achtung-baby-remastered/id%s?uo=4' % U2_ACHTUNGBABY_ID
U2_ONE_URL = 'https://itunes.apple.com/us/album/one/id%s?i=%s&uo=4' % (U2_ACHTUNGBABY_ID, U2_ONE_ID)


def test_search_track():
    assert itunes.search_track('u2 achtung baby one')[0].id == U2_ONE_ID


def test_search_album():
    assert itunes.search_album('u2 achtung baby')[0].id == U2_ACHTUNGBABY_ID


def test_search_artist():
    assert itunes.search_artist('u2')[0].id == U2_ID


def test_search_artist_store():
    U2_URL_ES = 'https://itunes.apple.com/es/artist/u2/id78500?l=en&uo=4'
    assert itunes.search_artist('u2', store='ES')[0].id == U2_ID
    assert itunes.search_artist('u2', store='ES')[0].url == U2_URL_ES


def test_lookup_track():
    item = itunes.lookup(U2_ONE_ID)
    assert isinstance(item, itunes.Track)
    assert item.id == U2_ONE_ID
    assert item.name == U2_ONE

    assert item.album.id == U2_ACHTUNGBABY_ID
    assert item.artist.id == U2_ID


def test_lookup_album():
    item = itunes.lookup(U2_ACHTUNGBABY_ID)
    assert isinstance(item, itunes.Album)
    assert item.id == U2_ACHTUNGBABY_ID
    assert item.name == U2_ACHTUNGBABY

    assert item.artist.id == U2_ID


def test_lookup_artist():
    item = itunes.lookup(U2_ID)
    assert isinstance(item, itunes.Artist)
    assert item.id == U2_ID
    assert item.name == U2


def test_lookup_notfound():
    UNKNOWN_ID = 0
    with pytest.raises(itunes.ITunesException):
        itunes.lookup(UNKNOWN_ID)


def test_artist_url():
    item = itunes.lookup(U2_ID)
    assert item.url == U2_URL


def test_album_url():
    item = itunes.lookup(U2_ACHTUNGBABY_ID)
    assert item.url == U2_ACHTUNGBABY_URL


def test_track_url():
    item = itunes.lookup(U2_ONE_ID)
    assert item.url == U2_ONE_URL


def test_album_length():
    item = itunes.lookup(U2_ACHTUNGBABY_ID)
    assert isinstance(item.get_tracks(), list)


def test_unicode():
    assert itunes.search_artist('Björk')[0].id == itunes.search_artist(u'Bj\xf6rk')[0].id


def test_unicode2():
    assert itunes.search_artist('Björk')[:5] == itunes.search_artist(u'Bj\xf6rk')[:5]


def test_movie_as_track():
    item = itunes.search(query='the godfather', media='movie')[0]
    assert item.artist == None
