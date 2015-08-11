""" murls (Mutable URL Strings): an expressive way to manipulate URLs. """

from collections import UserString


class Url(UserString):
    """ The base class for Mutable URL Strings. """

    _specs = ('{schema}://'
              '{username}{colon1}{password}{at}'
              '{host}{colon2}{port}'
              '{forward_slash}{path}'
              '{question_mark}{query}'
              '{hash}{fragment}')

    def __init__(self, *args, **kwargs):
        super(Url, self).__init__(*args, **kwargs)

        self._schema = str()
        self._host = str()
        self._path = list()
        self._query = dict()
        self._fragment = str()

        # Not yet implemented
        self._username = str()
        self._password = str()
        self._port = 0

    def host(self, host):
        self._host = host
        self.data = self._build()
        return self

    def schema(self, schema):
        self._schema = schema
        self.data = self._build()
        return self

    def fragment(self, fragment):
        self._fragment = fragment
        self.data = self._build()
        return self

    def path(self, *path):
        self._path = path
        self.data = self._build()
        return self

    def query(self, **parameters):
        self._query.update(parameters)
        self.data = self._build()
        return self

    @property
    def _parts(self):
        return {'schema': self._schema,
                'username': self._username,
                'colon1': self._colon1,
                'password': self._password,
                'host': self._host,
                'colon2': self._colon2,
                'port': str(self._port) if self._port else '',
                'forward_slash': self._forward_slash,
                'path': '/'.join(self._path),
                'question_mark': self._question_mark,
                'query': '&'.join([str(k) + '=' + str(v) for k, v in self._query.items()]) if self._query else '',
                'hash': self._hash,
                'fragment': self._fragment,
                'at': self._at}

    def _build(self):
        return self._specs.format(**self._parts)

    @staticmethod
    def port(port):
        raise NotImplemented('Cannot insert port %s' % port)

    @staticmethod
    def username(username):
        raise NotImplemented('Cannot insert username %s' % username)

    @staticmethod
    def password(password):
        raise NotImplemented('Cannot insert password %s' % password)

    @property
    def _colon1(self):
        return ':' if self._password else ''

    @property
    def _colon2(self):
        return ':' if self._port else ''

    @property
    def _at(self):
        return '@' if self._username else ''

    @property
    def _hash(self):
        return '#' if self._fragment else ''

    @property
    def _question_mark(self):
        return '?' if self._query else ''

    @property
    def _forward_slash(self):
        return '/' if self._path else ''

    @property
    def _left_bracket(self):
        return '[' if self._username else ''

    @property
    def _right_bracket(self):
        return ']' if self._username else ''

    def __contains__(self, item):
        return item in self.data


class Http(Url):
    def __init__(self, *args, **kwargs):
        super(Http, self).__init__(*args, **kwargs)
        self._schema = 'http'
        self._host = args[0]
        self.data = self._build()


class Https(Url):
    def __init__(self, *args, **kwargs):
        super(Https, self).__init__(*args, **kwargs)
        self._schema = 'https'
        self._host = args[0]
        self.data = self._build()


def http(site):
    return Http(site)


def https(site):
    return Https(site)


if __name__ == '__main__':
    url = http('cdkjkljbelkvbfl').path('jknjnk').query(foo='bar')
    print(url)
