# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
#import utils.database as db_utils


class Headers:

    def __init__(self, page):
        self._page = page


    def _get_content(self):
        return str(_page.content).replace("'", "")


    def _get_headers(self, page):
        return str(_page.headers).replace("'", "")


    def _has_xframe_defence(self):
        try:
        	xframe = self._get_headers()['x-frame-options']
        	print('X-FRAME-OPTIONS:', xframe , 'present')
        	return True
        except:
        	print('X-FRAME-OPTIONS missing')
        	return False


    def _has_hsts_defence(self):
        try:
        	hsts = self._get_headers()['Strict-Transport-Security']
        	print('Strict-Transport-Security:', hsts , 'present')
        	return True
        except:
        	print('HSTS header not set')
        	return False


    def _has_x_content_type_options_defence(self):
        try:
        	x_content_type_options = self._get_headers()['X-Content-Type-Options']
        	if x_content_type_options == 'no-sniff':
        	    print('X-Content-Type-Options:', x_content_type_options , 'present')
        	    return True

        	print('HSTS header not set')
        except:
        	print('HSTS header not set')
        	return False
