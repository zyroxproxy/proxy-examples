"""Run several sticky sessions in parallel — one IP per worker.

Session names are unlimited; use a different name per worker.
"""
import os
from concurrent.futures import ThreadPoolExecutor

import requests

USER = os.environ["ZYROX_USER"]
PASS = os.environ["ZYROX_PASS"]


def fetch(worker_id: int) -> tuple[int, str]:
    proxy = (
        f"http://{USER}-country-us-session-worker{worker_id}:{PASS}"
        "@host.zyroxproxy.com:7000"
    )
    r = requests.get(
        "https://api.ipify.org",
        proxies={"http": proxy, "https": proxy},
        timeout=30,
    )
    return worker_id, r.text


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as pool:
        for worker_id, ip in pool.map(fetch, range(1, 6)):
            print(f"worker {worker_id}: {ip}")
