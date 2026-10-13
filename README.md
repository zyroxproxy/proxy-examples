# Zyrox Proxy: Code Examples

Ready-to-run examples for using [Zyrox Proxy](https://zyroxproxy.com) residential, datacenter and mobile proxies with **cURL, Python (requests, Playwright, Selenium, Scrapy), Node.js (fetch, Playwright, Puppeteer), Go, PHP and Java**.

Zyrox is a standard proxy: anything that speaks HTTP or SOCKS5 works unmodified. 70M+ IPs across 180+ countries, rotating or sticky sessions, pay-as-you-go [from $2/GB](https://zyroxproxy.com/pricing/).

## Connection details

| | |
|---|---|
| Host | `host.zyroxproxy.com` |
| HTTP / HTTPS port | `7000` |
| SOCKS5 port | `7001` |
| Credentials | Proxy username + password from your [dashboard](https://zyroxproxy.com/dashboard) |

Options ride in the **username** as `-key-value` pairs:

```
USERNAME-country-us-session-abc123-sessiontime-60:PASSWORD@host.zyroxproxy.com:7000
```

| Option | Example | Meaning |
|---|---|---|
| `country` | `-country-us` | Exit country (ISO 3166-1 alpha-2, lowercase) |
| `session` | `-session-abc123` | Sticky IP: same name, same IP. Omit for a new IP on every request |
| `sessiontime` | `-sessiontime-60` | Sticky duration in minutes (default 30, max 120). Requires `session` |

City, state, ZIP and ASN targeting are also available; see [Geo targeting](https://docs.zyroxproxy.com/targeting/).

## Setup

Copy `.env.example` to `.env` and fill in your proxy credentials, or export them:

```bash
export ZYROX_USER=your-proxy-username
export ZYROX_PASS=your-proxy-password
```

## Examples

| Folder | What it shows |
|---|---|
| [`curl/`](curl/examples.sh) | Rotating, country, sticky, session duration, SOCKS5 |
| [`python/requests_example.py`](python/requests_example.py) | A small helper that builds proxy URLs from options |
| [`python/concurrent_sessions.py`](python/concurrent_sessions.py) | Parallel sticky sessions, one IP per worker |
| [`python/playwright_example.py`](python/playwright_example.py) | Headless Chromium through the proxy |
| [`scrapy/`](scrapy/) | A downloader middleware for whole-crawl proxying with optional sticky sessions |
| [`nodejs/fetch-example.js`](nodejs/fetch-example.js) | Node 18+ `fetch` via undici `ProxyAgent` |
| [`nodejs/playwright-example.js`](nodejs/playwright-example.js) | One IP per browser context |
| [`nodejs/puppeteer-example.js`](nodejs/puppeteer-example.js) | Chrome `--proxy-server` + `page.authenticate()` |
| [`python/selenium_example.py`](python/selenium_example.py) | Selenium Chrome with an auth extension |
| [`go/main.go`](go/main.go) | `net/http` client, parallel sticky sessions with goroutines |
| [`php/curl_example.php`](php/curl_example.php) | PHP cURL: country, sticky session, SOCKS5 |
| [`php/guzzle_example.php`](php/guzzle_example.php) | Guzzle with a URL-encoded password |
| [`java/ZyroxProxyExample.java`](java/ZyroxProxyExample.java) | Java 11+ `HttpClient`, no dependencies |

```bash
# Python
cd python && pip install -r requirements.txt && python requests_example.py

# Node.js
cd nodejs && npm install && npm run fetch

# Scrapy
cd scrapy && pip install scrapy && scrapy crawl ip_check

# Go
cd go && go run .

# PHP
cd php && php curl_example.php
cd php && composer install && php guzzle_example.php

# Java 11+
cd java && java ZyroxProxyExample.java
```

Every example hits `https://api.ipify.org`, which returns the exit IP, so you can see rotation and sticky sessions working.

## Tips

- **Quote the proxy URL** in shells; it can contain characters the shell treats specially.
- **Use `socks5h://`** (not `socks5://`) with curl so DNS resolves at the exit, not locally.
- **Sticky IPs are held, not frozen.** A residential device can go offline mid-session, so build in retries.
- Up to **2,000 concurrent connections** per account; above that you get `429 Too Many Connections`.

## Links

- 🌐 [zyroxproxy.com](https://zyroxproxy.com)
- 📚 [Documentation](https://docs.zyroxproxy.com) · [Integrations](https://docs.zyroxproxy.com/integrations/)
- ❓ [Help Center](https://help.zyroxproxy.com)
- 📧 support@zyroxproxy.com

Use only for lawful collection of public data, in line with our [Acceptable Use Policy](https://zyroxproxy.com/aup/).

## License

[MIT](LICENSE)
