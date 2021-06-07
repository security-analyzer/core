# -*- coding: utf-8 -*-

class XSSProtectionScanner:

    def __init__(self, headers):
        self._headers = headers


    def has_xxs_protection_vuls(self):
        try:
            xxs_protection = self._headers['X-XSS-Protection']
            return xxs_protection == 0
        except:
            return True