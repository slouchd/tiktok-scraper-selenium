#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from userlookup import TikTokProfile


def no_webdriver_path():
    lookup = TikTokProfile.get_tiktok_profile("abba", "chrome")
    data = json.loads(lookup)
    print(json.dumps(data))


def with_webdriver_path():
    lookup = TikTokProfile.get_tiktok_profile("abba", "chrome", "/usr/local/bin/chromedriver")
    data = json.loads(lookup)
    print(json.dumps(data))


no_webdriver_path()
with_webdriver_path()