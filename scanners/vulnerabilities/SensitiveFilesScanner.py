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
            response = requests.get(self._website + '/' + file)

            if response and response.status_code != 400:
                print(file)
                return True
            
        return False