# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import utils.Utils as _utils

class Contents:

    def __init__(self, contents):
        self._contents = contents

    def has_iframe_sandboxing_defence(self):
        try:
            soup = BeautifulSoup(self._contents, features="html.parser")
            iframes = soup.findAll('iframe')
            if len(iframes) == 0:
                return True

            for iframe in iframes:
                if iframe.get('sandboxs') is None:
                    return False

            return True
        except:
            return False


    def has_csrf_tokens_defence(self):
        try:
            tokens = ['csrf', 'token', 'nonce']
            soup = BeautifulSoup(self._contents, features="html.parser")
            forms = soup.findAll('form')
            if len(forms) == 0:
                return True

            for form in forms:
                hidden_inputs = form.find_all("input", type="hidden")
                for hidden_input in hidden_inputs:
                    if _utils.contains_one_of(hidden_input.get('name'), tokens) and hidden_input.get('value').isalnum():
                        return True

            return False
        except:
            return False
