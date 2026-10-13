BOT_NAME = "zyrox_example"
SPIDER_MODULES = ["zyrox_example.spiders"]

ZYROX_COUNTRY = "us"

# The Zyrox middleware must run before HttpProxyMiddleware (750).
DOWNLOADER_MIDDLEWARES = {
    "zyrox_example.middlewares.ZyroxProxyMiddleware": 749,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 750,
}

ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 8
DOWNLOAD_TIMEOUT = 30
RETRY_TIMES = 3
