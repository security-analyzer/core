# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class RemoteJavascriptScanner:

    def __init__(self, website, body):
        self._body = body
        self._domain = urlparse(website).netloc

    def _trusted_domains(self):
        return [
            self._domain,
            'https://cdnjs.cloudflare.com',
            'https://polyfill'
        ]


    def has_remote_javascript_vuls(self):
        soup = BeautifulSoup(self._body, features="html.parser")

        scriptTags = soup.findAll('script')
        for tag in scriptTags:
            url = tag.get('src')
            for domain in self._trusted_domains():
                if (url is not None) and (domain in url):
                    return False

            return True

        return False