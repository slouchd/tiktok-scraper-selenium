#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import selenium
from fake_headers import Headers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class TikTokProfile():
    def chrome_driver(webdriver_path=None):
        # Generate a fake user agent
        ua = Headers().generate()

        browser_options = ChromeOptions()
        browser_options.add_argument("--headless")
        browser_options.add_argument("--incognito")
        browser_options.add_argument("--log-level=3")
        browser_options.add_argument("--disable-gpu")
        browser_options.add_argument("--disable-extensions")
        browser_options.add_argument("--disable-notifications")
        browser_options.add_argument("--disable-popup-blocking")
        browser_options.add_argument(f"user-agent={ua}")

        if webdriver_path is not None:
            driver = webdriver.Chrome(
                service=ChromeService(executable_path=f"{webdriver_path}"),
                options=browser_options
            )
        else:
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=browser_options
            )

        return driver


    def firefox_driver(webdriver_path=None):
        # Generate a fake user agent
        ua = Headers().generate()

        browser_options = FirefoxOptions()
        browser_options.add_argument("--headless")
        browser_options.add_argument("--incognito")
        browser_options.add_argument("--log-level=3")
        browser_options.add_argument("--disable-gpu")
        browser_options.add_argument("--disable-extensions")
        browser_options.add_argument("--disable-notifications")
        browser_options.add_argument("--disable-popup-blocking")
        browser_options.add_argument(f"user-agent={ua}")

        if webdriver_path is not None:
            driver = webdriver.Firefox(
                service=FirefoxService(executable_path=f"{webdriver_path}"),
                options=browser_options
            )
        else:
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=browser_options
            )

        return driver


    def init_driver(browser_name, webdriver_path=None):
        if browser_name.lower() == "chrome":
            return TikTokProfile.chrome_driver(webdriver_path)
        elif browser_name.lower() == "firefox":
            return TikTokProfile.firefox_driver(webdriver_path)
        else:
            return "Browser not supported. Choose either Chrome of Firefox..."


    def get_tiktok_profile(username, browser_name, webdriver_path=None):
        profile_url = f"https://tiktok.com/@{username}"

        try:
            driver = TikTokProfile.init_driver(browser_name, webdriver_path)
            driver.get(profile_url)
        except AttributeError:
            print(f"Web driver of choice ({browser_name}) is not set")

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.title_contains(f"@{username}"))

        # Location of data on page to extract from
        state_data = driver.execute_script("return window['SIGI_STATE']")
        user_data = state_data["UserModule"]["users"][username.lower()]
        stats_data = state_data["UserModule"]["stats"][username.lower()]

        # Create json blob of profile
        profile_data = {}
        profile_data["username"] = user_data["uniqueId"]
        profile_data["nickname"] = user_data["nickname"]
        profile_data["uid"] = user_data["id"]
        profile_data["secuid"] = user_data["secUid"]
        profile_data["description"] = user_data["signature"]
        profile_data["verified"] = user_data["verified"]
        profile_data["private"] = user_data["privateAccount"]
        profile_data["avatarlarge"] = user_data["avatarLarger"]
        profile_data["avatarmedium"] = user_data["avatarMedium"]
        profile_data["avatarthumb"] = user_data["avatarThumb"]
        profile_data["followers"] = stats_data["followerCount"]
        profile_data["following"] = stats_data["followingCount"]
        profile_data["videos"] = stats_data["videoCount"]
        profile_data["hearts"] = stats_data["heartCount"]

        driver.close()
        driver.quit()

        return json.dumps(profile_data)