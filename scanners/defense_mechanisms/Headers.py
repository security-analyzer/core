# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class Headers:

    def __init__(self, headers):
        self._headers = headers

    def has_xframe_defence(self):
        try:
            xframe = self._headers['X-Frame-Options']
            return True
        except:
            return False

    def has_hsts_defence(self):
        try:
            hsts = self._headers['Strict-Transport-Security']
            return True
        except:
            return False

    def has_x_content_type_options_defence(self):
        try:
            x_content_type_options = self._headers['X-Content-Type-Options']
            if x_content_type_options == 'no-sniff' or x_content_type_options == 'nosniff':
                return True

            return False
        except:
            return False

    def has_http_only_defence(self):
        try:
            set_cookie = self._headers['Set-Cookie']
            if 'httponly' in set_cookie.lower():
                return True

            return False
        except:
            return False

    def has_secure_cookie_defence(self):
        try:
            set_cookie = self._headers['Set-Cookie']
            if 'secure' in set_cookie.lower():
                return True

            return False
        except:
            return False

    def has_content_security_policy_defence(self):
        try:
            csp = self._headers['Content-Security-Policy']
            return True
        except:
            return False

