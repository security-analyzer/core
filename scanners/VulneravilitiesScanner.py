class VulneravilitiesScanner:
    
    def __init__(self, website, headers, body):
        self._website = website
        self._headers = headers
        self._body = body