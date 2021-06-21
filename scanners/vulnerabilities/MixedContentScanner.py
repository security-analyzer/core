# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class MixedContentScanner:

    def __init__(self, body):
        self._body = body


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


    def has_mixed_content_vuls(self):
        soup = BeautifulSoup(self._body, features="html.parser")

        for tagName, attributes in self._tags().items():
            tags = soup.findAll(tagName)
            for tag in tags:
                for attribute in attributes:
                    url = tag.get(attribute)
                    if (url is not None) and 'http://' in url:
                        return True

        return False