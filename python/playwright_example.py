"""Zyrox Proxy with Playwright (Python).

pip install -r requirements.txt && playwright install chromium
Credentials go in username/password, not inside `server`.
"""
import os

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        proxy={
            "server": "http://host.zyroxproxy.com:7000",
            "username": f"{os.environ['ZYROX_USER']}-country-us-session-pw1",
            "password": os.environ["ZYROX_PASS"],
        }
    )
    page = browser.new_page()
    page.goto("https://api.ipify.org")
    print("Exit IP:", page.text_content("body"))
    browser.close()
