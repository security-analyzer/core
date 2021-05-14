# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup


class Headers:

    def __init__(self, headers):
        self._headers = headers


    def has_xframe_defence(self):
        print(self._headers['X-Frame-Options'])
        try:
        	xframe = self._headers['X-Frame-Options']
        	print('X-FRAME-OPTIONS:', xframe , 'present')
        	return True
        except:
        	print('X-FRAME-OPTIONS missing')
        	return False


    def has_hsts_defence(self):
        try:
        	hsts = self._headers['Strict-Transport-Security']
        	print('Strict-Transport-Security:', hsts , 'present')
        	return True
        except:
        	print('HSTS header not set')
        	return False


    def has_x_content_type_options_defence(self):
        try:
            x_content_type_options = self._headers['X-Content-Type-Options']
            if (x_content_type_options == 'no-sniff' or x_content_type_options == 'nosniff'):
                print('X-Content-Type-Options:', x_content_type_options , 'present')
                return True

            print('HSTS header not set')
            return False
        except:
        	print('HSTS header not set')
        	return False
