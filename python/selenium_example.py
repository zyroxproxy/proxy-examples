"""Zyrox Proxy with Selenium (Chrome).

Chrome's --proxy-server flag cannot carry a username and password, so this
builds a tiny extension that answers the proxy's auth challenge.

pip install selenium
python selenium_example.py
"""
import os
import zipfile

from selenium import webdriver

USERNAME = f"{os.environ['ZYROX_USER']}-country-us-session-sel1"
PASSWORD = os.environ["ZYROX_PASS"]

MANIFEST = """{
  "version": "1.0.0",
  "manifest_version": 3,
  "name": "Zyrox Proxy Auth",
  "permissions": ["webRequest", "webRequestAuthProvider"],
  "host_permissions": ["<all_urls>"],
  "background": { "service_worker": "background.js" }
}"""

BACKGROUND = """
chrome.webRequest.onAuthRequired.addListener(
  () => ({ authCredentials: { username: %s, password: %s } }),
  { urls: ["<all_urls>"] },
  ["blocking"]
);
""" % (repr(USERNAME), repr(PASSWORD))

EXTENSION = "zyrox_auth.zip"
with zipfile.ZipFile(EXTENSION, "w") as z:
    z.writestr("manifest.json", MANIFEST)
    z.writestr("background.js", BACKGROUND)

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://host.zyroxproxy.com:7000")
options.add_extension(EXTENSION)

driver = webdriver.Chrome(options=options)
try:
    driver.get("https://api.ipify.org")
    print("Exit IP:", driver.find_element("tag name", "body").text)
finally:
    driver.quit()
    os.remove(EXTENSION)
