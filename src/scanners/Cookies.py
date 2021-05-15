# -*- coding: utf-8 -*-


class Cookies:

    def __init__(self, cookie):
        self._cookie = cookie

    def has_http_only(self):
        extra_args = self._cookie.__dict__.get('_rest')
        if extra_args:
            for key in extra_args.keys():
                if key.lower() == 'httponly':
                    return True

        return False