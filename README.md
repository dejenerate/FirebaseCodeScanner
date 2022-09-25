# FirebaseCodeScanner
Scans repos for open firebase databases that can be read publicly

FirebaseCodeScanner searches for open Firebase databases hardcoded into various repositories and checks if they are open to public read access. Open Firebase databases leave corporate data accessible to anyone on the internet. The scanner uses the SearchCode.com API (free to use) to scan for open databases with security misconfigurations.

If the Firebase database returns a server response 200, it would be reviewed. The scanner displays open databases in red as it runs in the terminal. A properly configured database should return a 401 server response, which means that the request is unauthorized. If the database no longer exists, the server response will be a 404.

Here is a video of FirebaseCoderScanner executing:

https://replayable.io/replay/63277764f1e66e0068733f44/?share=GOIokM2Cmkj3KQiRqWjMJA

## How to use
The following syntax executes the search all repositories:

**firesearch.py**


The following syntax searches a specific repo:

**firesearch.py -r <repo_name>**


**Note that if the API does not find the repo given in the parameter, it will continue the search and find all repositories with hardcoded firebase databases.**

### Command-Line Parameters (Optional)

-h
The -h command-line parameter lists help options for the scanner. There is only one parameter at the movement, so the help menu displays one option.

-r <repository_name>

The -r parameter will scan a specific repository for open Firebase databases. Use this parameter to find open Firebase databases within a repository’s list of projects.

