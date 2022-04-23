import requests
from pprint import pprint
import re
import validators
from termcolor import colored
import os
from colorama import Fore, Back, Style, init
import sys, getopt

init()

"""
#Get command line options
"""
url = ""
flag_repo = 0
repo_name = ""

if len(sys.argv) > 1:
    long_options = ["help", "repo="]
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:", long_options)
    except Exception as e:
        print(e)
        print ('Error in command syntax. The right syntax is firesearch.py or firesearch -r <repository name>. Type firesearch.py -h for an example.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('To search all repositories for open firebase databases, the correct syntax is: firesearch.py. \nUse firesearch.py -r <repository_name> to search a specific repository.')
            print ('Example: firesearch.py will search all public repositories for open firebase databases.')
            print('Example: firesearch.py -r myexample  will search for open firebase databases in the myexample repository.')
            sys.exit(2)
        elif opt == "-r":
            flag_repo = 1
            url = "https://searchcode.com/api/codesearch_I/?q=.firebaseio.com%20repo:" + arg + "&p=0&per_page=50"
            repo_name = arg
        else:
            url = "https://searchcode.com/api/codesearch_I/?q=.firebaseio.com&p=0&per_page=50"
else:
    url = "https://searchcode.com/api/codesearch_I/?q=.firebaseio.com&p=0&per_page=50"

print(colored(url, 'cyan'))
response = requests.get(url)
res = response.json()
totalRecords = res['total']
languages = res['language_filters']
results = res['results']
record = 0
previousDatabase = ""
os.system('color')

print("total lines found: " + str(totalRecords))

#get number of pages based on 100 output per page
pages = int(totalRecords/50)
#pages = 3

for i in range(pages):
    print("page" + str(i))
    if i != 0:
        if flag_repo == 0:
            response = requests.get("https://searchcode.com/api/codesearch_I/?q=.firebaseio.com&p=" + str(i) + "&per_page=50")
        else:
            response = requests.get("https://searchcode.com/api/codesearch_I/?q=.firebaseio.com%20repo:" + repo_name + "&p=" + str(i) + "&per_page=50")

        res = response.json()
        results = res['results']

        if results is None:
            print(colored(response.json(), 'yellow'))
            continue

    for result in results:
        location = result['location']

        # loop through lines with firebase database
        lines = result['lines']
        for key, value in lines.items():
            if ".firebaseio.com" in value:
                database = re.search("https://(.*?).firebaseio.com", value)
                if database:
                    if database[0] != previousDatabase:
                        previousDatabase = database[0]
                        valid = validators.url(database[0] + "/.json")
                        if valid:
                            # get server response
                            try:
                                openDb = requests.get(database[0] + "/.json", timeout=5)
                            except Exception as e:
                                print(colored(e, 'yellow'))
                                continue
                            else:
                                record += 1
                                if openDb.status_code == 200:
                                    print(colored(
                                        str(record) + ".  REPO: " + result['repo'] + "  LOCATION: " + location + " DB: " + database[
                                            0] + "/.json" + " -------->" + str(openDb.status_code), 'red'))
                                else:
                                    print(
                                        str(record) + ".  REPO: " + result['repo'] + "  LOCATION: " + location + " DB: " + database[
                                            0] + "/.json" + " -------->" + str(openDb.status_code))

                                openDb.close()

