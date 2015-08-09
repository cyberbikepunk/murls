""" murls: mutable URL strings. """

from collections import UserString


class Url(UserString):
    pass


class Http(Url):
    pass


class Https(Url):
    pass


class Ftp(Url):
    pass


class Ftps(Url):
    pass


def test_murls():
    pass
