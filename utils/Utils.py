import json
from Wappalyzer import Wappalyzer, WebPage

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


def extract_server(url):
    webpage = WebPage.new_from_url(url)
    wappalyzer = Wappalyzer.latest()
    techs = wappalyzer.analyze_with_versions_and_categories(webpage)
    # print(techs)
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
    webpage = WebPage.new_from_url(url)
    wappalyzer = Wappalyzer.latest()
    techs = wappalyzer.analyze_with_versions_and_categories(webpage)
    for key in techs:
        if 'CMS' in techs[key]['categories']:
            version = False
            try:
                version = techs[key]['versions'][techs[key]['categories'].index('CMS')]
            except:
                version: False
            return {'CMS': key, 'version': version}
    return False