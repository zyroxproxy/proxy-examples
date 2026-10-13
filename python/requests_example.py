"""Zyrox Proxy with Python requests.

pip install -r requirements.txt
Set ZYROX_USER and ZYROX_PASS in your environment, then run:
python requests_example.py
"""
import os

import requests

USER = os.environ["ZYROX_USER"]
PASS = os.environ["ZYROX_PASS"]
HOST = "host.zyroxproxy.com:7000"


def proxy_url(**params: str) -> str:
    """Build a proxy URL. Options ride in the username as -key-value pairs."""
    username = USER + "".join(f"-{k}-{v}" for k, v in params.items())
    return f"http://{username}:{PASS}@{HOST}"


def get_ip(proxy: str) -> str:
    r = requests.get(
        "https://api.ipify.org",
        proxies={"http": proxy, "https": proxy},
        timeout=30,
    )
    r.raise_for_status()
    return r.text


if __name__ == "__main__":
    print("Rotating:      ", get_ip(proxy_url()), get_ip(proxy_url()))
    print("United States: ", get_ip(proxy_url(country="us")))

    sticky = proxy_url(country="gb", session="demo1", sessiontime="60")
    print("Sticky (GB):   ", get_ip(sticky), get_ip(sticky))
