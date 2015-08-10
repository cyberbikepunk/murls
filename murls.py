""" murls: mutable URL strings. """

from collections import UserString


class Url(UserString):
    """ The base class for Mutable URL Strings. """

    def __init__(self, *args, **kwargs):
        super(Url, self).__init__(*args, **kwargs)

        self._scheme = ''
        self._username = ''
        self._password = ''
        self._domain = args[0]
        self._host = ''
        self._ip = ''
        self._port = ''
        self._path = ''
        self._query = ''
        self._fragment = ''

    def __contains__(self, item):
        return item in self.data

    def path(self, *tree):
        self._path = '/'.join(tree)
        self.data = self._build()
        return self

    def query(self, **parameters):
        self._query = parameters
        self.data = self._build()
        return self

    def port(self):
        pass

    def username(self):
        pass

    def password(self):
        pass

    @property
    def colon(self):
        return ':' if self._password else ''

    @property
    def _at(self):
        return '@' if self._username else ''

    @property
    def _hash(self):
        return '#' if self._query else ''

    @property
    def _question_mark(self):
        return '?' if self._query else ''

    @property
    def _end_slash(self):
        return '/' if self._path else ''

    def _build(self):
        return self._scheme + self._host + self._end_slash + self._path + self._question_mark + self._query + self._hash + self._fragment


class Http(Url):
    def __init__(self, *args, **kwargs):
        super(Http, self).__init__(*args, **kwargs)
        self._scheme = 'http://'
        self._host = args[0]
        self.data = self._build()


class Https(Url):
    def __init__(self, *args, **kwargs):
        super(Https, self).__init__(*args, **kwargs)
        self._scheme = 'https://'
        self._host = args[0]
        self.data = self._build()


def http(site):
    return Http(site)


def https(site):
    return Https(site)


if __name__ == '__main__':
    pass