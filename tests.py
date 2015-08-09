""" Test suite for the murls module. """

from pytest import

from .murls import http, https, ftp, ftps


def test_instantiation():
    assert http('site.com') == 'http://site.com'
    assert ftp('site.com') == 'ftp://site.com'
    assert https('site.com') == 'https://site.com'
    assert ftps('site.com') == 'ftps://site.com'
    

def test_path():
    url = http('site.com')
    assert url.path(foo, bar) == 'http://site.com/bar/foo'
    assert url.path(foo) == 'http://site.com/foo'


def test_query():
    url = http('site.com')
    assert url.query(foo='bar', bar='foo') == 'http://site.com?foo=bar&bar=foo'
    assert url.query(foo='foo') == 'http://site.com?foo=foo&bar=foo'


def test_file():
    url = http('site.com')
    assert url.file('foo.bar') == 'http://site.com/foo.bar'


def test_validate():
    pass