murls
=====
Mutable URL strings.

Usage
-----
```python
from murls import http

site = 'zoo.com'
clade = ('felidae', 'panthera')
species = {'dangerous': 'true', 'social': 'true'}

url = http(site).path(*clade).query(**species)
# 'http://zoo.com/felidae/panthera?dangerous=true&social=false'

url.query(dangerous='false', origin='asia', social=None)
# 'http://zoo.com/felidae/panthera?dangerous=false&origin=asia'
```

Info
----
Installation: `pip install murls`. Sure, __murls__ reinvents the wheel. It was intended as an mini-exercise in API design. See the docstrings for details. [Apache2 Licensed](http://www.apache.org/licenses/LICENSE-2.0). 

