import scrapy


class IpCheckSpider(scrapy.Spider):
    """scrapy crawl ip_check: shows rotating vs sticky exit IPs."""

    name = "ip_check"

    def start_requests(self):
        for i in range(3):
            # Rotating: a fresh IP each time.
            yield scrapy.Request(
                "https://api.ipify.org",
                dont_filter=True,
                cb_kwargs={"label": f"rotating-{i}"},
            )
        for i in range(3):
            # Sticky: same session name, same IP.
            yield scrapy.Request(
                "https://api.ipify.org",
                dont_filter=True,
                meta={"zyrox_session": "spider1"},
                cb_kwargs={"label": f"sticky-{i}"},
            )

    def parse(self, response, label):
        yield {"label": label, "ip": response.text}
