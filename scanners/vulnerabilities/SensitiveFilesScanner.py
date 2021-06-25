import requests
import utils.Utils as _utils

class SensitiveFilesScanner:

    def __init__(self, website):
        self._website = website

    
    def _sensitive_files(self):
        return [
            '.git',
            '.svn', 
            '.well-known/',
            'phpinfo.php',
            'test.php',
            'Web.config',
            '.gitignore'
        ]

    
    def has_sensitive_files_vuls(self):
        sensitive_files = self._sensitive_files()
        for file in sensitive_files:
            url = self._website + file if self._website.endswith('/') else self._website + '/' + file
            response = requests.get(url, verify=False)

            if response and response.status_code != 400:
                print(file)
                return True
            
        return False