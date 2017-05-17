import urllib2
import json
import os
from pprint import pprint

REST_URL = "http://semanticportal.esipfed.org:8080"
# Insert your API Key here
API_KEY = ""

def get_json(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    return json.loads(opener.open(url).read())

terms = ['iceberg']

# Do a search for every term
search_results = []
for term in terms:
    search_results.append(get_json(REST_URL + "/search?q=" + term + "&ontologies=&include_properties=false&include_views=false&includeObsolete=false&require_definition=false&exact_match=false&categories=")["collection"])

# Print the results
for result in search_results:
    pprint(result)
