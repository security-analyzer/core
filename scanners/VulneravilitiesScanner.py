from crawlers.PageScrapper import PageScrapper
import scanners.vulnerabilities.MixedContentScanner as _mixed_content_vuls_scanner
import scanners.vulnerabilities.RemoteJavaScriptScanner as _remote_javascript_vuls_scanner
import scanners.vulnerabilities.SSLStrippingFormScanner as _ssl_striping_vuls_scanner
import scanners.vulnerabilities.XSSProtectionScanner as _xss_protection_vuls_scanner
import scanners.vulnerabilities.OutdatedCMSScanner as _outdated_cms_vuls_scanner
import scanners.vulnerabilities.OutdatedServerSoftwareScanner as _outdated_software_vuls_scanner
import scanners.vulnerabilities.SensitiveFilesScanner as _sensitive_files_vuls_scanner


class VulneravilitiesScanner:

    def __init__(self, website, pages):
        self._website = website
        self._pages = pages
        self._results = []
        self._untested_websites = []


    def handle_scan_process(self):
        try:
            page_scrapper = PageScrapper(self._website, self._pages)
            pages = page_scrapper.get_results()

            has_outdated_cms_vuls = _outdated_cms_vuls_scanner.OutdatedCMSScanner(self._website).has_outdated_cms_vuls()
            has_outdated_server_software_vuls = _outdated_software_vuls_scanner.OutdatedServerSoftwareScanner(self._website).has_outdated_server_software_vuls()
            has_sensitive_files_vuls = _sensitive_files_vuls_scanner.SensitiveFilesScanner(self._website).has_sensitive_files_vuls()
                
            for page in pages:
                print("Start scanning: " + page.get_link())
                print(page.get_link())
                result = dict()
                result['url'] = page.get_link()
                result['type'] = 'vulneravilities'
                result['results'] = dict()
                result['results']['has_mixed_content_vuls'] = _mixed_content_vuls_scanner.MixedContentScanner(page.get_content()).has_mixed_content_vuls()
                result['results']['has_remote_javascript_vuls'] = _remote_javascript_vuls_scanner.RemoteJavascriptScanner(self._website, page.get_content()).has_remote_javascript_vuls()
                result['results']['has_ssl_tripping_form_vuls'] = _ssl_striping_vuls_scanner.SSLStrippingFormScanner(page.get_content()).has_ssl_tripping_form_vuls()
                result['results']['has_xxs_protection_vuls'] = _xss_protection_vuls_scanner.XSSProtectionScanner(page.get_headers()).has_xxs_protection_vuls()
                result['results']['has_outdated_cms_vuls'] = has_outdated_cms_vuls
                result['results']['has_outdated_server_software_vuls'] = has_outdated_server_software_vuls
                result['results']['has_sensitive_files_vuls'] = has_sensitive_files_vuls
                self._results.append(result)
        except:
            self._untested_websites.append(self._website)


    def get_scan_results(self):
        return self._results

    
    def get_untested_websites(self):
        return self._untested_websites