""" Test suite for the murls module. """


from murls import http, https


def test_init():
    assert http('site.com') == 'http://site.com'
    assert https('site.com') == 'https://site.com'


def test_path():
    url = http('site.com')
    assert url.path('foo', 'bar') == 'http://site.com/foo/bar'
    assert url.path('foo') == 'http://site.com/foo'


def test_query():
    url = http('site.com')
    assert url.query(foo='bar', bar='foo') == 'http://site.com?foo=bar&bar=foo' or 'http://site.com?bar=foo&foo=bar'
    assert url.query(foo='foo') == 'http://site.com?foo=foo&bar=foo' or 'http://site.com?bar=foo&foo=foo'

