# -*- coding: utf-8 -*-

class Headers:

    def __init__(self, headers):
        self._headers = headers

    def has_xframe_defence(self):
        try:
            xframe = self._headers['X-Frame-Options']
            print('X-FRAME-OPTIONS:', xframe, 'present')
            return True
        except:
            print('X-FRAME-OPTIONS missing')
            return False

    def has_hsts_defence(self):
        try:
            hsts = self._headers['Strict-Transport-Security']
            print('Strict-Transport-Security:', hsts, 'present')
            return True
        except:
            print('HSTS header not set')
            return False

    def has_x_content_type_options_defence(self):
        try:
            x_content_type_options = self._headers['X-Content-Type-Options']
            if x_content_type_options == 'no-sniff' or x_content_type_options == 'nosniff':
                print('X-Content-Type-Options:', x_content_type_options, 'present')
                return True

            print('HSTS header not set')
            return False
        except:
            print('HSTS header not set')
            return False

    def has_http_only_defence(self):
        try:
            set_cookie = self._headers['Set-Cookie']
            if 'httponly' in set_cookie.lower():
                print('Set-Cookie: HttpOnly is present')
                return True

            print('The Set-Cookie: HttpOnly is missing')
            return False
        except:
            print('The Set-Cookie: HttpOnly is missing')
            return False

    def has_secure_cookie_defence(self):
        try:
            set_cookie = self._headers['Set-Cookie']
            if 'secure' in set_cookie.lower():
                print('Set-Cookie: Secure is present')
                return True

            print('The Set-Cookie: Secure is missing')
            return False
        except:
            print('The Set-Cookie: Secure is missing')
            return False

    def has_content_script_policy_defence(self):
        try:
            csp = self._headers['Set-Cookie']
            print('Content-Script-Policy is present')
            return True
        except:
            print('Content-Script-Policy is missing')
            return False
