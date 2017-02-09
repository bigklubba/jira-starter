#!/usr/bin/env python3


import sys
import webbrowser

WEBBROWSER = 'firefox'
JIRA_PATH = 'jira.ist.com/browse/'


def main():
    url_path = 'http://jira.ist.com/secure/Dashboard.jspa'
    if len(sys.argv) > 1:
        url_path = JIRA_PATH + sys.argv[1]

    webbrowser.get(WEBBROWSER).open_new_tab(url_path)

main()
