# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class MixedContentScanner:

    def __init__(self, contents):
        self._contents = contents


    def _tags(self):
        return {
            'audio': ['src'],
            'embed': ['src'],
            'form': ['action'],
            'iframe': ['src'],
            'img': ['src', 'srcset', 'data-src'],
            'link': ['href'],
            'object': ['data'],
            'param': ['value'],
            'script': ['src'],
            'source': ['src', 'srcset'],
            'video': ['src']
        }


    def extract_mixed_content_urls(self):
        soup = BeautifulSoup(self._contents, features="html.parser")
        mixed_content_urls = []

        for tagName, attributes in self._tags().items():
            tags = soup.findAll(tagName)
            for tag in tags:
                for attribute in attributes:
                    print()
