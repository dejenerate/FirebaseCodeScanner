# FirebaseCodeScanner
Scans repos for open firebase databases that can be read publicly

This is a simple scanner that uses SearchCode API to find firebase databases in source code and checks to see if the database is misconfigured to allow read access publicly.

## How to use
The following syntax executes the search all repositories:

**firesearch.py**


The following syntax searches a specific repo:

**firesearch.py -r <repo_name>**


**Note that if the API does not find the repo given in the parameter, it will continue the search and find all repositories with hardcoded firebase databases.**
