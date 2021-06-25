import utils.Utils as _utils

class OutdatedCMSScanner:

    def __init__(self, website):
        self._website = website

    
    def _oudated_cms(self):
        return {
            'joomla': [
                '1.0',
                '1.5',
                '1.6',
                '1.7',
                '2.5',
                '3.0',
                '3.1',
                '3.2',
                '3.3',
                '3.4',
                '3.5',
                '3.6',
                '3.7',
                '3.8',
            ],
            'wordpress': [
                '0.7',
                '1.0',
                '1.2',
                '1.5',
                '2.0',
                '2.1',
                '2.2',
                '2.3',
                '2.5',
                '2.6',
                '2.7',
                '2.9',
                '3.0',
                '3.1',
                '3.2',
                '3.3',
                '3.4',
                '3.5',
                '3.6'
            ],
            'drupal': [
                '6.38',
                '5.23'
            ],
            'prestashop': [
                '1.6'
            ],
            'magento': [
                '1.0',
                '1.1',
                '1.2',
                '1.3',
                '1.4',
                '1.5',
                '1.6',
                '1.7',
                '1.8',
                '1.9',
                '2.0',
                '2.1',
                '2.2',
                '2.3',
                '2.4'
            ]
        }

    def has_outdated_cms_vuls(self):
        cms_website = _utils.extract_cms(self._website)
        if (cms_website == False) or (cms_website['version'] == False):
            return False

        for cms in self._oudated_cms():
            if cms.lower() in cms_website['CMS'].lower():
                for cms_version in self._oudated_cms()[cms]:
                    if cms_version in cms_website['version']:
                        return True

        return False