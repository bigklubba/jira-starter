#!/usr/bin/env python

__author__ = 'piem7783'
import sys
import webbrowser

WEBBROWSER = 'firefox'
JIRA_PATH = 'merlin.hrm.local/jira/browse/UTV-'

def main():
  url_path = 'http://merlin/jira/secure/Dashboard.jspa'
  if len(sys.argv) > 1:
    url_path = JIRA_PATH + sys.argv[1]

  webbrowser.get(WEBBROWSER).open_new_tab(url_path)
main()
