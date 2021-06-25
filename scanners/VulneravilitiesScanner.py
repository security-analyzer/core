from crawlers.PageScrapper import PageScrapper
import scanners.vulnerabilities.RemoteJavaScriptScanner as _remote_javaScript_scanner


class VulneravilitiesScanner:

    def __init__(self, website, pages):
        self._website = website
        self._pages = pages
        self._results = []

    
    def handle_scan_process(self):
        page_scrapper = PageScrapper(self._website, self._pages)
        pages = page_scrapper.get_results()
        
        for page in pages:
            page.get_headers()
            # headers_scanner = _headers_scanner.Headers(page_headers)
            # contents_scanner = _body_scanner.Body(page.get_content())
            # result = dict()
            # result['has_mixed_content_vuls'] = _remote_javaScript_scanner.
            # result['has_remote_javascript_vuls'] = headers_scanner.has_x_content_type_options_defence()
            # result['has_ssl_tripping_form_vuls'] = headers_scanner.has_hsts_defence()
            # result['has_xxs_protection_vuls'] = headers_scanner.has_secure_cookie_defence()
            # result['has_outdated_cms_vuls'] = headers_scanner.has_http_only_defence()
            # result['has_outdated_server_software_vuls'] = contents_scanner.has_iframe_sandboxing_defence()
            # result['has_sensitive_files_vuls'] = contents_scanner.has_csrf_tokens_defence()
            # self._results.append(result)


    def get_scan_results(self):
        return self._results