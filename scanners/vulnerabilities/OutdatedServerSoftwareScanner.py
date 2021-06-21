import utils.Utils as _utils

class OutdatedServerSoftwareScanner:

    def __init__(self, website):
        self._website = website

    
    def _oudated_servers(self):
        return {
            'IIS': [
                '6.0'
            ],
            'nginx': [
                '1.18.0', 
                '1.16.1', 
                '1.14.2', 
                '1.12.2', 
                '1.10.3', 
                '1.8.1', 
                '1.6.3', 
                '1.4.7', 
                '1.2.9', 
                '1.0.15',
                '0.8.55',
                '0.7.69',
                '0.6.39',
                '0.5.38'
            ],
            'apache': [
                '1.3'
            ],
            'tomcat': [
                '3.0',
                '3.1',
                '3.2',
                '3.3',
                '4.0',
                '4.1',
                '5.0',
                '5.5'
            ]
        }

    def has_outdated_server_software_vuls(self):
        webserver = _utils.extract_server(self._website)
        if (webserver == False) or (webserver['version'] == False):
            return False

        for server in self._oudated_servers():
            if server.lower() in webserver['server'].lower():
                for server_version in self._oudated_servers()[server]:
                    if server_version in webserver['version']:
                        return True

        return False