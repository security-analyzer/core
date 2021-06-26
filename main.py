from datetime import datetime
import scanners.DefenseMechanismsScanner as _defense_mechanisms_scanner
import scanners.VulneravilitiesScanner as _vulneravilities_scanner
import utils.Utils as _utils
from multiprocessing import Process, Queue
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def hand_scan_for_category(category_id, scan_id):
    print(scan_id)
    print('============ category ' + str(category_id) + ' =========================')
    websites = _utils.find_websites_by_category_name(category_id)
    for website in websites:
        defense_mechanisms_scanner = _defense_mechanisms_scanner.DefenseMechanismsScanner(website['website'], website['pages'])
        defense_mechanisms_scanner.handle_scan_process()
        scan_results = defense_mechanisms_scanner.get_scan_results()
        _utils.save_scan_results_by_scan_id(scan_id, scan_results)
        print(scan_results)
        print('\n\n strt defs ====================================================================')
        print(defense_mechanisms_scanner.get_untested_websites())
        print('\n\nend def ====================================================================')


        vulneravilities_scanner_scanner = _vulneravilities_scanner.VulneravilitiesScanner(website['website'], website['pages'])
        vulneravilities_scanner_scanner.handle_scan_process()
        scan_results = vulneravilities_scanner_scanner.get_scan_results()
        _utils.save_scan_results_by_scan_id(scan_id, scan_results)
        # print(scan_results)
        print('\n\n strt vuls ====================================================================')
        print(vulneravilities_scanner_scanner.get_untested_websites())
        print('\n\nend vuls ====================================================================')


# # Run vuls and defense mechanisms scanners
if __name__ == "__main__":
    
    new_scan = _utils.create_new_scan('Scan 1')
    queue = Queue()

    start_time = time.time()
    categories = _utils.find_categories()
    processes = [Process(target=hand_scan_for_category, args=(category[1], new_scan[0])) for category in categories[:1]]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


def init_database():
    vuls = [
        'has_mixed_content_vuls',
        'has_mixed_content_vuls',
        'has_remote_javascript_vuls',
        'has_ssl_tripping_form_vuls',
        'has_xxs_protection_vuls',
        'has_outdated_cms_vuls',
        'has_outdated_server_software_vuls',
        'has_sensitive_files_vuls',
    ]

    defences = [
        'has_xframe',
        'has_x_content_type_options',
        'has_hsts',
        'has_secure_cookie',
        'has_http_only',
        'has_iframe_sandboxing',
        'has_csrf_tokens',
    ]

    for vul in vuls:
        query = "INSERT INTO `rules`(`name`, `type`) VALUES ('" + vul + "','vulneravility')"
        _utils.commit_query(query)

    for defense in defences:
        query = "INSERT INTO `rules`(`name`, `type`) VALUES ('" + defense + "','defense_mechanism')"
        _utils.commit_query(query)

    categories_with_websites = [
        {
            'category': 'Secteur public',
            'websites': [
                'http://www.parlement.ma',
                'http://www.conseil-constitutionnel.ma',
                'https://www.diplomatie.ma',
                'http://www.justice.gov.ma',
                'http://www.habous.gov.ma',
                'https://www.minculture.gov.ma',
                'https://mtataes.gov.ma',
                'https://www.sante.gov.ma',
                'https://www.mem.gov.ma',
                'https://www.mcinet.gov.ma',
                'https://www.mmsp.gov.ma',
                'http://www.mcrp.gov.ma',
                'http://www.equipement.gov.ma',
                'http://www.mincom.gov.ma',
                'http://marocainsdumonde.gov.ma',
            ],
            'pages': _utils.read_file_items('datasets/secteur_publique.txt')
        },
        {
            'category': 'Finance',
            'websites': [
                'https://www.douane.gov.ma',
                'https://www.tax.gov.ma',
                'https://www.cmr.gov.ma',
                'https://www.oc.gov.ma',
                'https://www.bmci.ma',
                'https://damanecash.ma',
                'https://www.creditdumaroc.ma',
                'https://www.umniabank.ma',
                'https://www.cihbank.ma',
                'https://attijarinet.attijariwafa.com',
                'http://www.baa.ma',
                'https://bpnet.gbp.ma',
                'https://www.wafasalaf.ma',
                'https://www.cashplus.ma',
                'https://www.sgmaroc.com',
            ],
            'pages': _utils.read_file_items('datasets/finance.txt')
        },
        {
            'category': 'Education',
            'websites': [
                'http://www.inscriptionupf.com',
                'http://www.aui.ma',
                'http://www.uae.ma',
                'https://www.uit.ac.ma',
                'http://www.uaq.ma',
                'http://www.uh1.ac.ma',
                'http://www.usmba.ac.ma',
                'https://www.uca.ma',
                'https://www.uiz.ac.ma',
                'http://www.chariaa.usmba.ac.ma',
                'https://www.uiass.ma',
                'http://www.flam.uca.ma',
                'http://www.flsh-uh2c.ac.ma',
                'http://www.fsts.ac.ma',
                'http://www.flsh-agadir.ac.ma',
            ],
            'pages': _utils.read_file_items('datasets/education.txt')
        },
        {
            'category': 'e-commerce',
            'websites': [
                'https://www.arganpalace.com',
                'http://www.parapharma.ma',
                'https://www.mahalkom.ma',
                'https://www.fleurs-maroc.ma',
                'https://www.avito.ma',
                'https://www.jumia.ma',
                'https://www.iris.ma',
                'https://www.mescadeaux.ma',
                'https://www.prixfous.ma',
                'http://www.richbond.ma',
                'https://www.lcwaikiki.ma',
                'https://www.youpi.co.ma',
                'https://www.abidcars.com',
                'http://www.aircar.ma',
                'https://www.decathlon.ma',
            ],
            'pages': _utils.read_file_items('datasets/ecommerce.txt')
        },
        {
            'category': "Alexa",
            'websites': [
                'https://www.chouftv.ma',
                'https://www.hespress.com',
                'https://www.2m.ma',
                'https://www.alayam24.com',
                'https://www.elbotola.com',
                'https://www.almaghreb24.com',
                'https://tanja24.com',
                'https://fr.le360.ma',
                'https://www.elhadat24.com',
                'http://www.akhbarona.com',
                'https://kech24.com',
                'https://www.immolist.ma',
                'https://www.moteur.ma',
                'https://agadir24.info',
                'https://www.anfaspress.com',
            ],
            'pages': _utils.read_file_items('datasets/alexa.txt')
        }
    ]

    for website_category in categories_with_websites:
        for website in website_category['websites']:
            pages = [] 
            for page in website_category['pages']:
                website_domain = website.replace('http://', '').replace('https://', '')
                if website_domain in page:
                    pages.append(page)
            _utils.insert_website_with_pages(website_category['category'], website, pages)
