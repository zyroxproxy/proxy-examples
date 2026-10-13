import os


class ZyroxProxyMiddleware:
    """Route every request through Zyrox Proxy.

    Country comes from the ZYROX_COUNTRY setting (default "us"). A spider can
    pin a sticky IP for a chain of requests with meta={"zyrox_session": "name"}.
    """

    def __init__(self, country: str):
        self.user = os.environ["ZYROX_USER"]
        self.password = os.environ["ZYROX_PASS"]
        self.country = country

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get("ZYROX_COUNTRY", "us"))

    def process_request(self, request, spider):
        username = f"{self.user}-country-{self.country}"
        session = request.meta.get("zyrox_session")
        if session:
            username += f"-session-{session}"
        request.meta["proxy"] = f"http://{username}:{self.password}@host.zyroxproxy.com:7000"
