import json

# Shared utils
def dict_to_json(dictionary):
    return json.dumps(dictionary, indent = 4)


def json_to_dict(json_object):
    return json.loads(json_object)


def contains_one_of(word, terms):
    for term in terms:
        if word in term:
            return True
    return False
