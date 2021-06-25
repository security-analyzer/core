from crawlers.PageScrapper import PageScrapper
import scanners.defense_mechanisms.Headers as _headers_scanner
import scanners.defense_mechanisms.Body as _body_scanner


class DefenseMechanismsScanner:

    def __init__(self, website, pages):
        self._website = website
        self._pages = pages
        self._results = []
        self._untested_websites = []

    
    def handle_scan_process(self):
        try:
            page_scrapper = PageScrapper(self._website, self._pages[:2])
            pages = page_scrapper.get_results()
            for page in pages:
                print("Start scanning: " + page.get_link())
                page_headers = page.get_headers()
                headers_scanner = _headers_scanner.Headers(page_headers)
                contents_scanner = _body_scanner.Body(page.get_content())
                result = dict()
                result['url'] = page.get_link()
                result['type'] = 'defense_mechanisms'
                result['results'] = dict()
                result['results']['has_xframe'] = headers_scanner.has_xframe_defence()
                result['results']['has_x_content_type_options'] = headers_scanner.has_x_content_type_options_defence()
                result['results']['has_hsts'] = headers_scanner.has_hsts_defence()
                result['results']['has_secure_cookie'] = headers_scanner.has_secure_cookie_defence()
                result['results']['has_http_only'] = headers_scanner.has_http_only_defence()
                result['results']['has_iframe_sandboxing'] = contents_scanner.has_iframe_sandboxing_defence()
                result['results']['has_csrf_tokens'] = contents_scanner.has_csrf_tokens_defence()
                self._results.append(result)
        except:
            self._untested_websites.append(self._website)


    def get_scan_results(self):
        return self._results
    

    def get_untested_websites(self):
        return self._untested_websites