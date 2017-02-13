# -*- coding: utf-8 -*-

import requests


def get(url):
    requests.get(url)


def get_by_ssl(url):
    requests.get(url, verify=False)
