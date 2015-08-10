""" Test suite for the murls module. """

import pytest

from .murls import http, https, ftp, ftps


def test_init():
    assert http('site.com') == 'http://site.com'
    assert https('site.com') == 'https://site.com'


@pytest.fixture
def url():
    return http('site.com')


def test_path(url):
    assert url.path('foo', 'bar') == 'http://site.com/bar/foo'
    assert url.path('foo') == 'http://site.com/foo'


def test_query(url):
    assert url.query(foo='bar', bar='foo') == 'http://site.com?foo=bar&bar=foo'
    assert url.query(foo='foo') == 'http://site.com?foo=foo&bar=foo'

