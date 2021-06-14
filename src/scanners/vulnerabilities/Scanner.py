# -*- coding: utf-8 -*-

class Scanner:

    def __init__(self, domain, headers, contents):
        self._domain = domain
        self._contents = contents
        self._headers = headers