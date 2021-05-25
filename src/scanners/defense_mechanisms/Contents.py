# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class Contents:

    def __init__(self, contents):
        self._contents = contents

    def has_iframe_sandboxing_defence(self):
        try:
            soup = BeautifulSoup(self._contents, features="html.parser")
            iframes = soup.findAll('iframe')
            if len(iframes) == 0:
                print('There\'s No iframe tag in this page')
                return True

            for iframe in iframes:
                if iframe.get('sandboxs') is None:
                    print('iframe sandboxing mechanism is missing')
                    return False

            print('iframe sandboxing is present')
            return True
        except:
            print('iframe sandboxing mechanism is missing')
            return False

