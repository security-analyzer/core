# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class SSLStrippingFormScanner:

    def __init__(self, contents):
        self._contents = contents


    def has_ssl_tripping_form_vuls(self):
        soup = BeautifulSoup(self._contents, features="html.parser")

        formTags = soup.findAll('form')
        for tag in formTags:
            url = tag.get('action')
            if (url is not None) and 'http://' in url:
                return True

        return False