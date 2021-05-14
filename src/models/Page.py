# -*- coding: utf-8 -*-

class Page:

    def __init__(self, website, link, headers={}, content={}):
        self._website = website
        self._link = link
        self._headers = headers
        self._content = content

    def get_website(self):
        return self._website

    def get_link(self):
        return self._link

    def get_content(self):
        return self._content

    def get_headers(self):
        return self._headers
