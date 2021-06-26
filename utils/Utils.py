# -*- coding: utf-8 -*-
import json
import ssl
from urllib.parse import quote
from Wappalyzer import Wappalyzer, WebPage
import mysql.connector
import urllib.request


# Shared utils
def dict_to_json(dictionary):
    return json.dumps(dictionary, indent = 4)


def json_to_array(json_values):
    return json.loads(json_values)


def json_to_dict(json_object):
    return json.loads(json_object)


def contains_one_of(word, terms):
    for term in terms:
        if term in word:
            return True
    return False


def urlopen(url, timeout=60):
    headers = {'User-Agent': 'Mozilla/5.0 Firefox/33.0'}
    req = urllib.request.Request(url, None, headers)
    return urllib.request.urlopen(req, timeout=timeout, context=ssl._create_unverified_context())


def tupes_to_dict(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


def extract_used_techs(url):
    # webpage = urlopen(url, 60)
    # content = webpage.read().decode('utf-8')
    # headers = dict(webpage.getheaders())
    # webpage = WebPage(url, html=content, headers=headers)#.new_from_url(url, verify=False)
    webpage = WebPage.new_from_url(url, verify=False)
    wappalyzer = Wappalyzer.latest()
    return wappalyzer.analyze_with_versions_and_categories(webpage)


def extract_server(url):
    techs = extract_used_techs(url)
    for key in techs:
        if 'Web servers' in techs[key]['categories']:
            version = False
            try:
                version = techs[key]['versions'][techs[key]['categories'].index('Web servers')]
            except:
                version = False

            return {'server': key, 'version': version}
    return False


def extract_cms(url):
    techs = techs = extract_used_techs(url)
    for key in techs:
        if 'CMS' in techs[key]['categories']:
            version = False
            try:
                version = techs[key]['versions'][techs[key]['categories'].index('CMS')]
            except:
                version: False
            return {'CMS': key, 'version': version}
    return False


def accepted_url(target, nlink):
    target_domain = target.replace('http://', '').replace('https://', '')
    target_domain_without_www = target_domain.replace('www.', '')
    page_url = nlink.split('/')[-1]
    if (not nlink.endswith('.pdf') and (not nlink.endswith('.PDF')) and (not nlink.endswith('.rtf')) and (not nlink.endswith('.pptx')) and not nlink.endswith('.docx')  and not nlink.endswith('.doc') and not nlink.endswith('.csv') and not nlink.endswith('.xlsx') and ('accounts.google.com') not in nlink) and (nlink.startswith('http://' + target_domain) or nlink.startswith('https://' + target_domain) or nlink.startswith('http://www.' + target_domain_without_www) or nlink.startswith('https://www.' + target_domain_without_www)) and ('.pdf' not in page_url) and ('download' not in nlink):
        return True
    return False


def read_file_items(file_path):
    file = open(file_path, "r")
    return file.readlines()


def fetch_all(query):
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="web_crawler"
    )

    query_cursor = database.cursor(buffered=True)
    query_cursor.execute(query)
    items = query_cursor.fetchall()
    database.close()
    return items


def fetch_one(query):
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="web_crawler"
    )

    query_cursor = database.cursor(buffered=True)
    query_cursor.execute(query)
    item = query_cursor.fetchone()
    database.close()
    return item


def commit_query(query):
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="web_crawler"
    )

    query_cursor = database.cursor()
    query_cursor.execute(query)
    database.commit()
    database.close()


def find_category_by_name(category_name):
    query = "SELECT * FROM categories WHERE name = '" + str(category_name) + "'"
    return fetch_one(query)


def find_website_by_url(url):
    query = "SELECT * FROM websites WHERE url = '" + str(url) + "'"
    return fetch_one(query)


def find_website_by_category_name(category_name):
    query = "SELECT websites.* FROM websites WHERE websites.category_id IN (SELECT categories.id FROM categories WHERE categories.name = '" + str(category_name) + "')"
    return fetch_one(query)


def find_websites_by_category_name(category_name):
    query = "SELECT websites.id, websites.url FROM websites WHERE websites.category_id IN (SELECT categories.id FROM categories WHERE categories.name = '" + str(category_name) + "')"
    websites = fetch_all(query)
    website_with_pages = []
    for website in websites:
        query = "SELECT url FROM pages WHERE website_id = '" + str(website[0]) + "'"
        website_pages = fetch_all(query)
        pages = []
        for page in website_pages:
            pages.append(page[0])
        website_with_pages.append({'website': website[1], 'pages': pages})
    return website_with_pages


def find_web_pages_by_category_name(category_name):
    website = find_website_by_category_name(category_name)
    if website:
        query = "SELECT * FROM pages WHERE website_id = '" + str(website[0]) + "'"
        return fetch_all(query)

    return []


def insert_website_with_pages(category_name, website_url = '', pages = []):
    category = find_category_by_name(category_name)
    if not category:
        query = "INSERT INTO categories (name) VALUES ('" + category_name + "')"
        commit_query(query)
        category = find_category_by_name(category_name)

    website = find_website_by_url(website_url)
    if not website:
        query = "INSERT INTO websites (url, category_id) VALUES ('" + str(website_url) + "', '" + str(category[0]) + "')"
        commit_query(query)
        website = find_website_by_url(website_url)
    
    for page in pages:
        page = page.replace("'", "\\'").replace("\n", '')
        print(page)
        query = "INSERT INTO pages (url, website_id) VALUES ('" + str(page) + "', '" + str(website[0]) + "')"
        commit_query(query)


def find_websites():
    query = "SELECT * FROM websites"
    return fetch_all(query)


def find_categories():
    query = "SELECT * FROM categories"
    return fetch_all(query)


def create_new_scan(label = ''):
    query = "INSERT INTO scans (label) VALUES ('" + str(label) + "')"
    commit_query(query)
    return fetch_one("SELECT * FROM scans ORDER BY id DESC LIMIT 1")


def fin_rule_id_by_name(rule_name):
    query = "SELECT * FROM rules WHERE name = '" + str(rule_name) + "'"
    return fetch_one(query)[0]


def fin_page_id_by_url(page_url):
    query = "SELECT * FROM pages WHERE url LIKE '" + str(page_url) + "'"
    return fetch_one(query)[0]


def save_scan_page(scan_id, page_id):
    query = "INSERT INTO `scan_page`(`page_id`, `scan_id`) VALUES ('" + str(page_id) + "','" + str(scan_id) + "')"
    commit_query(query)
    return fetch_one("SELECT * FROM scan_page ORDER BY id DESC LIMIT 1")


def save_scan_results(scan_page_id, rule_id, value):
    is_secure = 1 if value else 0
    query = "INSERT INTO `scan_page_results`(`scan_page_id`, `rule_id`, `is_secure`) VALUES ('" + str(scan_page_id) + "','" + str(rule_id) + "','" + str(is_secure) + "')"
    commit_query(query)
    return fetch_one("SELECT * FROM scan_page_results ORDER BY id DESC LIMIT 1")


def save_scan_results_by_scan_id(scan_id, results = []):
    for result in results:
        page_id = fin_page_id_by_url(result['url'])
        scan_page = save_scan_page(scan_id, page_id)
        for key, value in result['results'].items():
            rule_id = fin_rule_id_by_name(key)
            scan_result = save_scan_results(scan_page[0], rule_id, value)
